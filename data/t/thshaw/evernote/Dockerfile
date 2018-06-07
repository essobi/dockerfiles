# Run evernote windows app in a container with wine  
#  
# docker run -d \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \  
# -e DISPLAY=unix$DISPLAY \  
# --name evernote \  
# thshaw/evernote  
#  
FROM thshaw/wine  
MAINTAINER thshaw <tom@tomwillfixit.com>  
  
COPY Evernote_5.8.13.8152.exe /usr/src/evernote.exe  
COPY start.sh /start.sh  
  
ENTRYPOINT ["bash", "/start.sh"]  

