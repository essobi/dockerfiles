# inspired by https://hub.docker.com/r/maestroalubia/trac/~/dockerfile/  
FROM python:2.7-alpine  
  
# Set the working directory to /app  
WORKDIR /app  
  
# Copy the necessary files to the container  
ADD requirements.txt /app  
  
# Install the requirements  
RUN apk update && \  
apk add --virtual build-deps gcc python-dev musl-dev && \  
apk add git postgresql-dev  
  
RUN pip install -r requirements.txt  
  
CMD /usr/local/bin/tracd -b 0.0.0.0 -p 80 -s /var/trac/dev.haiku-os.org  
  
# Make port 80 available to the outside world  
EXPOSE 80  

