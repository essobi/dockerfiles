FROM alpine:3.1  
MAINTAINER Ziv Rechnitser <ziv@devops.co.il>  
  
# Install server  
RUN apk add --update python py-pip  
  
# Temp port is 1234 need to change to spooler port  
EXPOSE 1234  
# Copy the application folder inside the container  
ADD /dummyspooler /var/lib/dummyspooler  
# ADD /docker-entrypoint.sh /usr/bin/docker-entrypoint.sh  
  
RUN pip install -r /var/lib/dummyspooler/requirements.txt  
  
WORKDIR /var/lib/dummyspooler  
  
CMD python main.py

