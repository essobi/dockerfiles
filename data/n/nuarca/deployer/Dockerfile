FROM nuarca/base  
MAINTAINER Shafqat Ahmed  
  
ENV ACCEPT_EULA Y  
ADD ./precheck.sh /app  
ADD ./doinstall.sh /app  
ADD ./dbscripts.zip /app  
ADD ./replace.js /app  
RUN cd /app && unzip dbscripts.zip  
RUN mkdir -p /app/config && mkdir -p /app/config/web && mkdir -p
/app/config/app  
ADD ./config/web/application.yml.template /app/config/web  
ADD ./config/web/application-prod.yml.template /app/config/web  
  
RUN mkdir -p /root/.ssh && echo StrictHostKeyChecking no > /root/.ssh/config  

