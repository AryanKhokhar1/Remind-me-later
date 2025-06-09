# Remind Me Later API (Assignment)

A REST API by DRF for creating reminder records.  
Users can schedule reminders with a message to be sent via SMS or Email at a specific date and time.

---

## Features

- Create reminders with a scheduled date and time.
- Supports sending reminders via SMS or Email.
- Reminders are stored and managed in UTC timezone.
- Simple REST endpoint to create reminders.

---

## Timezone

All reminders are scheduled and stored using **UTC timezone** internally.  

---

## Quick Start

1. Clone the repo:
   ```bash
   git clone https://github.com/AryanKhokhar1/Remind-me-later.git
   cd remind-me-later
   
2. Start Virtual Environment to start the project
   ```bash
   pip install virtualenv
   source env/bin/activate

---

## ScreenShots

1. Can't set Reminder in the past
![Screenshot from 2025-06-09 16-05-36](https://github.com/user-attachments/assets/d2f54802-a980-411a-8f45-33d0af1456ff)

2. Successfully set a reminder
![Screenshot from 2025-06-09 16-06-15](https://github.com/user-attachments/assets/f99127a2-4870-4f39-aa45-113bcdaab719)

3. Admin Panel
![Screenshot from 2025-06-09 16-21-02](https://github.com/user-attachments/assets/e39324fc-6fff-4ca2-ab92-9b4a4f2d3db4)

4. Reminder Model in Database
![Screenshot from 2025-06-09 16-20-52](https://github.com/user-attachments/assets/acdf8ee6-f393-4e66-8a0d-c01d83ba2696)
