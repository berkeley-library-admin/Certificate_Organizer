# =====================================================================
# MODULE 2: UI/UX DASHBOARD INTERFACE (WITH CLEAR ACTIONS)
# Purpose: Houses the layout, stylesheets, and dashboard control mechanics.
# =====================================================================

def generate_html_page(total_processed, last_batch_count, processed_text="", input_cache=""):
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Certificate Organizer</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            :root {{
                --bg-primary: #f8fafc;
                --surface: #ffffff;
                --text-main: #0f172a;
                --text-muted: #64748b;
                --accent: #4f46e5;
                --accent-hover: #4338ca;
                --success: #10b981;
                --danger: #ef4444;
                --danger-hover: #dc2626;
                --border: #e2e8f0;
            }}
            body {{ 
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                background-color: var(--bg-primary); color: var(--text-main); margin: 0; padding: 0; 
            }}
            .navbar {{
                background: var(--surface); padding: 16px 40px; border-bottom: 1px solid var(--border);
                display: flex; align-items: center; justify-content: space-between;
            }}
            .navbar h1 {{ font-size: 18px; margin: 0; font-weight: 600; }}
            .status-badge {{ background: #e0f2fe; color: #0369a1; padding: 4px 12px; border-radius: 9999px; font-size: 12px; font-weight: 600; }}
            .dashboard-container {{ max-width: 1200px; margin: 30px auto; padding: 0 20px; }}
            .stats-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 20px; margin-bottom: 30px; }}
            .stat-card {{ background: var(--surface); padding: 20px; border-radius: 12px; border: 1px solid var(--border); }}
            .stat-card .label {{ font-size: 13px; color: var(--text-muted); font-weight: 500; margin-bottom: 4px; }}
            .stat-card .value {{ font-size: 28px; font-weight: 700; }}
            .workspace-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 30px; }}
            @media (max-width: 768px) {{ .workspace-grid {{ grid-template-columns: 1fr; }} }}
            .panel {{ background: var(--surface); padding: 24px; border-radius: 12px; border: 1px solid var(--border); display: flex; flex-direction: column; }}
            .panel-header-row {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; }}
            .panel-title {{ font-size: 15px; font-weight: 600; margin: 0; }}
            textarea {{ width: 100%; height: 280px; padding: 14px; box-sizing: border-box; border: 1px solid var(--border); border-radius: 8px; font-size: 15px; line-height: 1.5; resize: none; font-family: inherit; }}
            textarea:focus {{ border-color: var(--accent); outline: none; box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1); }}
            .btn {{ background-color: var(--accent); color: white; padding: 12px 24px; border: none; border-radius: 8px; cursor: pointer; font-size: 15px; font-weight: 600; margin-top: 16px; transition: background 0.15s ease; text-align: center; }}
            .btn:hover {{ background-color: var(--accent-hover); }}
            .action-group {{ display: flex; gap: 8px; }}
            .btn-action {{ background-color: #f1f5f9; color: #475569; padding: 6px 14px; border: none; border-radius: 6px; cursor: pointer; font-size: 13px; font-weight: 600; transition: all 0.15s ease; }}
            .btn-action:hover {{ background-color: #e2e8f0;
