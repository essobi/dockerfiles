FROM python:3.6  
MAINTAINER Julian Kahnert <mail@juliankahnert.de>  
LABEL org.freenas.version="1" \  
org.freenas.autostart="true" \  
org.freenas.privileged="true" \  
org.freenas.expose-ports-at-host="false" \  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/app/config.json\", \  
\"descr\": \"dashbutton config file\" \  
} \  
]"  
  
VOLUME /app  
WORKDIR /app  
COPY . .  
  
# install dependencies  
RUN apt-get update  
RUN apt-get install -y \  
gcc \  
libnet1 \  
tcpdump  
  
RUN pip3 install --no-cache-dir -r requirements.txt  
  
CMD ["python3", "button.py"]  

