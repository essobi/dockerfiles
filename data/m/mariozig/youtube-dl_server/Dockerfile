FROM python:3.5-alpine  
  
RUN pip install --pre youtube_dl_server  
  
ENTRYPOINT ["youtube-dl-server", "--host=0.0.0.0"]  
  
LABEL maintainer="Mario Zigliotto <mariozig@gmail.com>"  

