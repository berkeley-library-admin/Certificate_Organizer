# =====================================================================
# MODULE 3: MAIN SERVER CONTROLLER (CLOUD DEPLOYMENT VERSION)
# Purpose: Directs local networking using environment-defined ports.
# =====================================================================

import http.server
import socketserver
import urllib.parse
import os

# Import our custom modules
import engine
import interface

# Global Tracking Stats (Reset on cloud container spin-down)
STATS = {
    "total_processed": 0,
    "last_batch_count": 0
}

class DashboardRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        
        html = interface.generate_html_page(STATS["total_processed"], STATS["last_batch_count"])
        self.wfile.write(html.encode("utf-8"))

    def do_POST(self):
        global STATS
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        
        parsed_data = urllib.parse.parse_qs(post_data)
        raw_names_string = parsed_data.get('student_names', [''])[0]
        
        lines = raw_names_string.splitlines()
        organized_list = []
        batch_counter = 0
        
        for line in lines:
            if line.strip():
                formatted = engine.format_certificate_name(line)
                batch_counter += 1
                organized_list.append(formatted)
                
        STATS["total_processed"] += batch_counter
        STATS["last_batch_count"] = batch_counter
        
        processed_output = "\n".join(organized_list)

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        
        html = interface.generate_html_page(
            STATS["total_processed"], 
            STATS["last_batch_count"], 
            processed_output, 
            raw_names_string
        )
        self.wfile.write(html.encode("utf-8"))

if __name__ == "__main__":
    # CRITICAL CLOUD LOGIC: Render tells our app what port to use via an environment variable.
    # Default to 8080 if running locally.
    PORT = int(os.environ.get("PORT", 8080))
    
    socketserver.TCPServer.allow_reuse_address = True
    
    # Bind to "" (all interfaces) so the cloud proxy can forward incoming global traffic
    with socketserver.TCPServer(("", PORT), DashboardRequestHandler) as httpd:
        print(f"🚀 Cloud Production Server Live on Port {PORT}")
        httpd.serve_forever()