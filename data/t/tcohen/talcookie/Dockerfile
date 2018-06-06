FROM python:3-alpine  
MAINTAINER Tal Cohen (tcohen@csh.rit.edu)  
  
# Install additional system packages required for some PYthon dependencies  
RUN apk add --no-cache postgresql-dev libffi-dev python-dev gcc musl-dev  
  
# Add application user  
RUN adduser -S talcookie && \  
mkdir -p /opt/talcookie  
  
# Add files and set permissions  
ADD . /opt/talcookie  
RUN chown -R talcookie /opt/talcookie  
WORKDIR /opt/talcookie  
  
# Install Python dependencies  
RUN pip install --no-cache-dir -r requirements.txt  
  
# Drop privileges  
USER talcookie  
  
# Expose the default server port  
EXPOSE 8080  
# Use gunicorn to serve the app  
CMD gunicorn --workers=2 --bind
${TALCOOKIE_SERVER_IP:-0.0.0.0}:${TALCOOKIE_SERVER_PORT:-8080} app  

