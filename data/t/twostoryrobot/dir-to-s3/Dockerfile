  
#  
# Dockerfile for daily directory backups to AWS S3  
#  
FROM ubuntu:latest  
MAINTAINER Chris Foster chris.james.foster@gmail.com  
WORKDIR /dir-to-s3  
  
# Install cron and AWS CLI  
RUN apt-get update \  
&& apt-get install -y cron python-pip python-dev build-essential \  
&& pip install awscli==1.11.35  
  
# Add files  
COPY crontab .  
COPY backup .  
COPY start .  
  
# Register crontab  
RUN crontab ./crontab  
  
# Create the upload directory  
RUN mkdir -p /upload  
  
CMD [ "/dir-to-s3/start" ]  

