FROM ubuntu  
  
MAINTAINER ynws  
  
RUN apt-get update && apt-get install -y fswebcam cron  
RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
  
ENV IMAGESIZE=1280x720 ROTATE=0  
COPY capture.sh /  
COPY cronSetting.sh /  
  
RUN env > /env  
CMD /bin/bash /capture.sh && ./cronSetting.sh 20 && cron -f  

