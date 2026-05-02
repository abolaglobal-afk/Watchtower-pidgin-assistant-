# Watchtower Pidgin English Study Assistant 📖

A beautiful, user-friendly web application for accessing Watchtower study materials with Pidgin English answers for each paragraph.

## ✨ Features

- 📱 **Beautiful Web Interface** - Easy to use on desktop, tablet, or mobile
- 🇳🇬 **Pidgin English Answers** - Responses in Pidgin for better understanding
- 📖 **Complete Study Content** - Paragraph text, answers, key points, and Bible references
- 🔍 **Quick Navigation** - Jump to any paragraph instantly
- 📱 **Responsive Design** - Works on all devices
- 🎯 **Study Themes** - Understand the focus of each study
- 💾 **Offline Ready** - Works without internet once loaded

## 🚀 Installation

### Requirements
- Python 3.7 or higher
- A web browser

### Setup Steps

1. **Clone or Download the Repository**
   ```bash
   git clone https://github.com/abolaglobal-afk/Watchtower-pidgin-assistant-.git
   cd Watchtower-pidgin-assistant-
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   python app.py
   ```

4. **Open in Your Browser**
   - Go to: `http://localhost:5000`
   - That's it! 🎉

## 📖 How to Use

### For Regular Users
1. Open the app in your browser
2. Select a study date from the dropdown
3. Read through the paragraphs
4. Click on any paragraph number to jump to it
5. Use the sidebar to navigate quickly

### Adding New Studies

Create a JSON file in the `data/watchtower/` directory with this format:

```json
{
  "publication": "Watchtower",
  "study_date": "2026-05-02",
  "title": "Study Title",
  "subtitle": "Study Subtitle",
  "study_theme": "Main Theme",
  "opening_comment": "Opening comment here",
  "closing_thoughts": "Closing thoughts here",
  "paragraphs": [
    {
      "number": 1,
      "text": "Original paragraph text from the Watchtower",
      "pidgin_answer": "Paragraph 1 answer in Pidgin English",
      "key_points": [
        "First key point",
        "Second key point"
      ],
      "cross_references": [
        "Matthew 5:3-12",
        "1 Peter 1:3-5"
      ]
    }
  ]
}
```

**File naming:** Use the study date as the filename: `2026-05-02.json`

## 📁 Project Structure

```
Watchtower-pidgin-assistant-/
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── README.md                # This file
├── watchtower_assistant.py  # Core assistant class
├── data/
│   └── watchtower/
│       └── sample_study.json    # Sample study template
├── templates/
│   ├── index.html          # Home page
│   └── study.html          # Study detail page
└── static/
    ├── style.css           # Styling
    └── script.js           # Interactive functionality
```

## 🎯 CLI Usage (For Advanced Users)

You can also use the command-line interface:

```bash
# List all available studies
python watchtower_assistant.py list

# View a complete study
python watchtower_assistant.py view --date 2026-05-02

# Get a specific paragraph answer
python watchtower_assistant.py answer --paragraph 1 --date 2026-05-02

# Get study summary
python watchtower_assistant.py summary --date 2026-05-02
```

## 🌐 API Endpoints (For Developers)

If you want to integrate with other applications:

- `GET /api/studies` - List all available studies
- `GET /api/study/<date>` - Get complete study data
- `GET /api/paragraph/<number>/<date>` - Get specific paragraph
- `GET /api/summary/<date>` - Get study summary

## 🔄 Updating Studies

Simply add new JSON files to `data/watchtower/` with the study date as the filename. They will automatically appear in the dropdown menu!

## 💡 Tips for Best Experience

1. **Mobile Friendly** - Open on your phone for convenient study access
2. **Print Ready** - Print any study directly from your browser
3. **Quick Navigation** - Use the paragraph buttons for instant jumping
4. **Share Studies** - Share the JSON files with others easily

## 🛠️ Troubleshooting

### "Study not found"
- Make sure your JSON file is in `data/watchtower/` directory
- Check that the filename matches the date format: `YYYY-MM-DD.json`

### Port Already in Use
- The app uses port 5000 by default
- Change it in `app.py`: `app.run(port=8000)`

### Slow Loading
- If you have many studies, the initial load might take a moment
- This is normal

## 📚 Example Study Structure

A typical study has:
- **18+ Paragraphs** (flexible - can have more or fewer)
- **Pidgin English Answers** - Explains the paragraph in simple Pidgin
- **Key Points** - Important takeaways
- **Bible References** - Relevant scripture passages
- **Theme** - The focus of the study
- **Opening & Closing Comments** - Introduction and wrap-up

## 🚀 Future Enhancements

- [ ] Search functionality
- [ ] Bookmark favorite paragraphs
- [ ] Notes taking feature
- [ ] Export to PDF
- [ ] Multiple language support
- [ ] Study comparison tools
- [ ] Progress tracking
- [ ] Mobile app (iOS/Android)

## 📝 License

This project is created for educational purposes to help Jehovah's Witnesses study Watchtower materials.

## 🙏 Support

For questions or suggestions, please open an issue on GitHub.

---

**Made with ❤️ for better understanding of Watchtower studies in Pidgin English**
