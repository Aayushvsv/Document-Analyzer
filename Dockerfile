# Stage 1: Use an official Python image as the base
# This line says, "Start with a clean computer that already has Python 3.12 installed."
FROM python:3.12-slim

# Stage 2: Set up the working directory inside the container
# This creates a folder inside our container called /code where we'll put our app
WORKDIR /code

# Stage 3: Copy dependency files and install them
# This copies the requirements file into the /code folder
COPY requirements.txt .

# This runs the pip install command inside the container.
# The --no-cache-dir is an optimization to keep the image smaller.
RUN pip install --no-cache-dir -r requirements.txt

# Stage 4: Copy the rest of the application code
# This copies our entire 'app' folder into the /code folder inside the container
COPY ./app /code/app

# Stage 5: Expose the port the app will run on
# This tells Docker that our application will be listening for traffic on port 8000
EXPOSE 8000

# Stage 6: Define the command to run the application
# This is the command that will be executed when the container starts.
# It's the same command we've been using, but formatted for Docker.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
