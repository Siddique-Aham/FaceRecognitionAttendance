from deepface import DeepFace
import cv2
import os
import csv
from datetime import datetime

# Configuration
DATA_FOLDER = "data"
ATTENDANCE_FILE = "attendance.csv"
DATE_FORMAT = "%Y-%m-%d"
TIME_FORMAT = "%H:%M:%S"

# Initialize attendance file with headers if not exists
if not os.path.exists(ATTENDANCE_FILE):
    with open(ATTENDANCE_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Date", "Time"])

def load_students():
    """Dynamically load students from data folder"""
    students = {}
    for img_file in os.listdir(DATA_FOLDER):
        if img_file.lower().endswith(('.png', '.jpg', '.jpeg')):
            name = os.path.splitext(img_file)[0]
            students[name] = os.path.join(DATA_FOLDER, img_file)
    return students

def mark_attendance(name):
    """Record attendance with proper formatting"""
    now = datetime.now()
    with open(ATTENDANCE_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            name,
            now.strftime(DATE_FORMAT),
            now.strftime(TIME_FORMAT)
        ])

def main():
    students = load_students()
    print(f"Loaded {len(students)} students: {', '.join(students.keys())}")
    
    video_capture = cv2.VideoCapture(0)
    attended_today = set()

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        try:
            # Face recognition
            results = DeepFace.find(
                img_path=frame,
                db_path=DATA_FOLDER,
                enforce_detection=False,
                silent=True
            )

            if results and len(results[0]) > 0:
                best_match = results[0].iloc[0]
                name = os.path.splitext(os.path.basename(best_match['identity']))[0]
                
                if name in students and name not in attended_today:
                    print(f"Attendance marked for {name}")
                    mark_attendance(name)
                    attended_today.add(name)
                    
                    # Visual feedback
                    cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 2)
                    cv2.putText(frame, name, (100, 90), 
                               cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        except Exception as e:
            print(f"Error: {e}")

        cv2.imshow('Attendance System', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()