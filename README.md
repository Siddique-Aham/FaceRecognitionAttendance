Face Recognition Attendance System

A Python-based attendance system that uses DeepFace for face recognition and OpenCV for real-time webcam capture. The system identifies students from a database of images, logs their attendance with date and time in a CSV file, and provides visual feedback during recognition.
Table of Contents

Features
Requirements
Installation
Project Structure
Usage
Contributing
License
Acknowledgments

Features

Real-time Face Recognition: Identifies students using DeepFace’s facial recognition model.
Automated Attendance Logging: Records attendance with name, date, and time in a CSV file.
Webcam Integration: Uses OpenCV to capture live video feed from a webcam.
Visual Feedback: Displays a green rectangle around detected faces with the student’s name.
Dynamic Student Database: Automatically loads student images from a data folder.
Error Handling: Gracefully handles face detection failures and other exceptions.
Prevent Duplicate Entries: Marks attendance only once per session for each student.

Requirements

Python 3.8 or higher
Webcam (built-in or external)
Image files (.png, .jpg, or .jpeg) of students in the data folder
Python libraries:
deepface
opencv-python



Installation

Clone the repository:
git clone https://github.com/Siddique-Aham/FaceRecognitionAttendance.git
cd FaceRecognitionAttendance


Install dependencies:Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install required packages:
pip install deepface opencv-python


Prepare the data folder:

Create a data folder in the project root.
Add student images named as <student_name>.jpg (e.g., JohnDoe.jpg).
Ensure images are in .png, .jpg, or .jpeg format.


Verify setup:Ensure your webcam is connected and functional.


Project Structure
FaceRecognitionAttendance/
├── data/
│   ├── tim.jpg
│   └── ...
├── attendance.py
├── requirements.txt
├── README.md
└── .gitignore


data/: Contains student images for face recognition.
attendance.py: Main script for the attendance system.
requirements.txt: Lists Python dependencies.
.gitignore: Excludes .csv files, Python cache, and virtual environments.
attendance.csv: Generated file for attendance logs (excluded from Git).

Usage

Run the script:
python attendance.py


What to expect:

The system loads student images from the data folder and displays the number of students loaded.
A webcam window opens, showing the live feed.
When a face is recognized, a green rectangle appears around it with the student’s name.
Attendance is logged in attendance.csv with the format:Name,Date,Time
JohnDoe,2025-06-22,01:59:00


Press q to quit the application.


View attendance:Open attendance.csv in a spreadsheet or text editor to review attendance records.


Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Make your changes and commit (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a pull request on GitHub.

Please ensure your code follows PEP 8 style guidelines and includes comments for clarity.
License
This project is licensed under the MIT License.
Acknowledgments

DeepFace for the face recognition library.
OpenCV for computer vision capabilities.
Inspired by the need for automated attendance systems in educational institutions.


Built with ❤️ by Siddique Aham
