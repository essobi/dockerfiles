# Pull base image.  
FROM python:3  
# Install ffmpeg.  
RUN \  
apt-get update && \  
apt-get install -y libav-tools && \  
rm -rf /var/lib/apt/lists/*  
  
EXPOSE 8080  
VOLUME ["/audio"]  
VOLUME ["/video"]  
  
RUN pip install bottle youtube-dl  
  
ADD . /app  
  
WORKDIR /app  
  
CMD [ "python", "-u", "./youtube-dl-server.py" ]  

