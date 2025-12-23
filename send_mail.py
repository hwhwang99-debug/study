import os
import markdown
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

FROM_EMAIL = os.environ["FROM_EMAIL"]
TO_EMAIL = os.environ["TO_EMAIL"]
APP_PASSWORD = os.environ["APP_PASSWORD"]

SUBJECT = "정책 뉴스 분석 보고서 초안"
MD_PATH = "policy_report_draft.md"

with open(MD_PATH, "r", encoding="utf-8") as f:
    md_text = f.read()

body_html = markdown.markdown(
    md_text,
    extensions=["extra", "tables", "nl2br"]
)

html_body = f"""
<html>
<body style="font-family: Apple SD Gothic Neo, Malgun Gothic, Arial, sans-serif; line-height:1.7;">
{body_html}
</body>
</html>
"""

msg = MIMEMultipart("alternative")
msg["From"] = FROM_EMAIL
msg["To"] = TO_EMAIL
msg["Subject"] = SUBJECT
msg.attach(MIMEText(html_body, "html", "utf-8"))

with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=20) as server:
    server.login(FROM_EMAIL, APP_PASSWORD)
    server.send_message(msg)

print("✅ 정책 보고서 메일 발송 완료")
