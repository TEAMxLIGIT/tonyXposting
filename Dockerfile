# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /usr/src/app
WORKDIR /usr/src/app

# Copy the requirements.txt and other necessary files
COPY requirements.txt ./
COPY tony ./tony

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variables
ENV API_ID=your_api_id
ENV API_HASH=your_api_hash
ENV BOT_TOKEN=your_bot_token
ENV OWNER_ID=your_owner_id
ENV SESSION_NAME=your_userbot_session_name

# Expose any ports your application needs
# EXPOSE 80

# Run the userbot when the container launches
CMD ["python", "./tony/__main__.py"]