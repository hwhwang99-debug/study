name: Send Policy Report Email

on:
  workflow_dispatch:
  schedule:
    - cron: "0 9 * * 1"   # 매주 월요일 09:00 UTC

jobs:
  send-mail:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: pip install markdown

      - name: Send policy report email
        env:
          FROM_EMAIL: ${{ secrets.FROM_EMAIL }}
          TO_EMAIL: ${{ secrets.TO_EMAIL }}
          APP_PASSWORD: ${{ secrets.APP_PASSWORD }}
        run: python send_mail.py
