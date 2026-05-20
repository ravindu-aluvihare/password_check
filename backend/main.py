from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import re

app = FastAPI()

# Allow frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PasswordRequest(BaseModel):
    password: str


class PasswordStrengthChecker:
    def __init__(self, password):
        self.password = password
        self.score = 0
        self.feedback = []

    def check_password(self):

        if len(self.password) >= 8:
            self.score += 1
        else:
            self.feedback.append("Password should be at least 8 characters")

        if len(self.password) >= 12:
            self.score += 1

        if re.search(r"[A-Z]", self.password):
            self.score += 1
        else:
            self.feedback.append("Add uppercase letter")

        if re.search(r"[a-z]", self.password):
            self.score += 1
        else:
            self.feedback.append("Add lowercase letter")

        if re.search(r"[0-9]", self.password):
            self.score += 1
        else:
            self.feedback.append("Add number")

        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", self.password):
            self.score += 1
        else:
            self.feedback.append("Add special character")

        return {
            "score": self.score,
            "feedback": self.feedback
        }


@app.post("/check-password")
def check_password(data: PasswordRequest):

    checker = PasswordStrengthChecker(data.password)

    return checker.check_password()