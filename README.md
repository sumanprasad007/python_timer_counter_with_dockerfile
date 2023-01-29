# Python Countdown Timer with Contaerization

This is a Python script that implements a countdown timer. The timer duration can be specified in seconds using an environment variable. If the environment variable is not set, the timer will default to 60 seconds.

Requirements
Docker
Dockerfile
# The following is the Dockerfile that can be used to build a Docker image for the countdown timer script:

bash
Copy code

FROM python:3.8-slim-buster

COPY countdown_timer.py /app/countdown_timer.py

WORKDIR /app

CMD ["python", "countdown_timer.py"]

# Execution Steps
Build the Docker image using the Dockerfile:
Copy code
  docker build -t countdown_timer .
  
# Run the Docker container and specify the timer duration using the TIMER_SECONDS environment variable:
css
Copy code
  docker run --name countdown_timer_container -e TIMER_SECONDS=<duration_in_seconds> countdown_timer
  
Replace <duration_in_seconds> with the desired timer duration in seconds.

The countdown timer will start running inside the container and will display the remaining time in the format mm:ss on the console, updating in real-time.

When the timer reaches 0, the message stop will be displayed.

Conclusion
This is a simple countdown timer script that can be easily run inside a Docker container. By specifying the timer duration using an environment variable, the script can be used for a variety of countdown scenarios without needing to modify the code.
