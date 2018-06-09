FROM python:3  
MAINTAINER Josh Mandel  
  
# Create the application directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install python dependencies  
COPY requirements.txt /usr/src/app/  
RUN pip install --no-cache-dir -r requirements.txt  
  
# Copy the codebase  
COPY . /usr/src/app  
  
# Configure the app  
ENV FLASK_APP "/usr/src/app/app.py"  
ENV FLASK_SECRET_KEY "SECRET"  
ENV SYNCHRONIZER_HOST "https://sync-api.demo.syncfor.science"  
ENV SYNCHRONIZER_USER "s4s-app"  
ENV SYNCHRONIZER_PASS "s4s-app-secret"  
CMD uwsgi uwsgi.ini  

