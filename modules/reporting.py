import json

def generate_report(data, format="json"):
    if format == "json":
        with open("report.json", "w") as f:
            json.dump(data, f, indent=4)
        print("✅ Report saved as report.json")
    elif format == "md":
        with open("report.md", "w") as f:
            f.write("# Security Report\n")
            f.write(json.dumps(data, indent=4))
        print("✅ Report saved as report.md")
    elif format == "html":
        with open("report.html", "w") as f:
            f.write("<html><body><h1>Security Report</h1>")
            f.write("<pre>" + json.dumps(data, indent=4) + "</pre>")
            f.write("</body></html>")
        print("✅ Report saved as report.html")
    else:
        print("❌ Invalid report format!")
