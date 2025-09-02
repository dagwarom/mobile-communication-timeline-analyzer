# Mobile Communication & Timeline Analyzer

## 📌 Description
Mobile Communication & Timeline Analyzer is a digital forensics tool to extract and analyze call logs & SMS from Android devices using ADB. It generates Excel reports with timestamps, contact details, and communication patterns, plus graphs of top contacts, aiding forensic timeline reconstruction.

---

## ✨ Features
- Extract Call Logs 📞
- Extract SMS Messages ✉️
- Timeline-based Analysis ⏳
- Export to Excel (.xlsx) 📊
- Graphs of Top Contacts 📈

---

## ⚙️ Installation
```bash
git clone https://github.com/dagwarom/mobile-communication-timeline-analyzer.git
cd mobile-communication-timeline-analyzer/src
pip install -r requirements.txt

python sms_extractor.py
python calllog_extractor.py

After this your file will be exported in .xlxs form you can even modify the code if you want to extract additional data.

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss.
