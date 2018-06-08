# Basic docker image for PokeAlarm  
# Usage:  
# docker build -t pokealarm .  
# docker run -d -P pokealarm  
FROM python:2.7-alpine  
  
# Default port the webserver runs on  
EXPOSE 4000  
# Working directory for the application  
WORKDIR /usr/src/app  
  
# Set Entrypoint with hard-coded options  
ENTRYPOINT ["python", "./runwebhook.py"]  
  
# Set default options when container is run without any command line arguments  
CMD ["-h"]  
  
# Install required system packages  
RUN apk add --no-cache ca-certificates  
RUN apk add --no-cache bash git openssh  
  
COPY requirements.txt /usr/src/app/  
  
RUN apk add --no-cache build-base \  
&& pip install --no-cache-dir -r requirements.txt \  
&& apk del build-base  
  
# Copy everything to the working directory (Python files, templates, config)
in one go.  
COPY . /usr/src/app/  

