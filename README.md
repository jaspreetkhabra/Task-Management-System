# Task Management Microservice - Logging Failed Login Attempts

## Overview
This microservice is responsible for logging failed login attempts in a task management system.

## Communication Contract
- **Endpoint:** `POST /log_attempt`
- **Request Format:**
  ```json
  {
    "user_id": "12345",
    "attempt_time": "2025-02-11T14:30:00Z",
    "status": "failed",
    "ip_address": "192.168.1.1",
    "device_info": "Windows 10, Chrome Browser"
  }
  
{
  "message": "Warning: Incorrect password entered for user 12345",
  "data": { ... }
}

## 🔄 UML Sequence Diagram
Below is the UML sequence diagram showing the interaction between the client, microservice, and database.

![UML Diagram]<img width="1063" alt="uml" src="https://github.com/user-attachments/assets/bf14be1d-ffb7-4df2-b961-941c483de0b2" />

