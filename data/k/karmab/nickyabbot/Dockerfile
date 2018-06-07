FROM gliderlabs/alpine:3.3  
MAINTAINER Karim Boumedhel <karimboumedhel@gmail.com>  
  
RUN apk add --no-cache python python-dev py-pip build-base \  
&& pip install PyTelegramBotAPI==2.2.3  
  
ADD nickyabbot.py /  
VOLUME ["/tmp/troll/.db"]  
  
CMD ["python", "-u", "/nickyabbot.py"]  

