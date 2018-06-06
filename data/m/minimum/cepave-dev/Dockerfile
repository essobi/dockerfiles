FROM docker:17.03  
  
# Set timezone  
RUN \  
apk add \--no-cache tzdata \  
&& cp /usr/share/zoneinfo/Asia/Taipei /etc/localtime \  
&& echo "Asia/Taipei" > /etc/timezone  
  
RUN \  
apk add -q --no-cache python3 \  
&& pip3 install -U pip docker-compose  
  

