FROM python:3.6.2-alpine  
LABEL org.freenas.interactive="false" \  
org.freenas.version="1.1.0" \  
org.freenas.expose-ports-at-host="false" \  
org.freenas.autostart="true" \  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/media\", \  
\"descr\": \"downloads folder\" \  
} \  
]" \  
org.freenas.settings="[ \  
{ \  
\"env\": \"TOKEN\", \  
\"descr\": \"TelegramAPI token\", \  
\"optional\": false \  
} \  
]"  
  
VOLUME /media  
  
# install youtube-dl  
RUN apk add --update youtube-dl  
  
# Copy the python files in the container  
COPY ./youtube-downloader.py /app/  
COPY ./requirements.txt /app/  
WORKDIR app  
  
# install the requirements  
RUN pip install --no-cache-dir -r requirements.txt  
  
# run the archiver  
CMD "python" "./youtube-downloader.py" "$TOKEN"  

