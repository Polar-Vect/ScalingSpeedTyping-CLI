
# ⌨️ TypeRush-CLI

> **Fast. Accurate. Clean.**  
> A minimalist terminal typing trainer designed to push your speed to the limit.

---

## 📝 Description
**TypeRush-CLI** is a high-speed typing challenge for your terminal. It presents random sentences that you must type as quickly and accurately as possible. The goal is to maintain a **Combo Streak** without making a single mistake.

## 🛠 Technologies
The project is built with **Python 3**, focusing on standard libraries for maximum compatibility:
*   `time` – For high-precision timing (milliseconds).
*   `random` – To provide a unique challenge every round.
*   `Standard I/O` – Optimized for the command-line interface.

## ⚙️ Functionality
The script follows a logical flow to ensure a smooth user experience:

1.  **Preparation:** A 3-second countdown ensures you are ready before the timer starts.
2.  **Precise Measurement:** The timer starts the exact millisecond the "GO!" signal appears and stops the moment you hit `Enter`.
3.  **Data Normalization:** Your input is compared using lowercase matching, so you can focus on speed rather than Shift-key precision.
4.  **Feedback Loop:** 
    *   **Success:** Displays your time in seconds (e.g., `4.52s`) and increments your combo.
    *   **Failure:** Shows where you tripped up and displays your final combo score.

## 🚀 Installation & Usage

### Prerequisites
*   Python 3.x installed on your machine.

## 🎮 Game Rules
*   **Wait for the Signal:** Don't start typing before the "GO!".
*   **Stay Accurate:** One wrong character ends your streak.
*   **Beat the Clock:** Try to get your time under 5 seconds for long sentences!

---

## 👥 Credits
*   **Adrian-weber7** - Original Logic , Concept & Refinement
*   **Polar** - Refinement & Expansion

---
*Developed for speed enthusiasts.*
