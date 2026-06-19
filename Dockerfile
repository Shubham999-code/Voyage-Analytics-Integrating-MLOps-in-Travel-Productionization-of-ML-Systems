# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose ports for Flask (5000) and Streamlit (8501)
EXPOSE 5000
EXPOSE 8501

# Define environment variable
ENV PYTHONUNBUFFERED=1

# Run Flask API using Gunicorn by default
# For Streamlit, you can override the command when running the container:
# docker run -p 8501:8501 myimage streamlit run streamlit_app.py
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
