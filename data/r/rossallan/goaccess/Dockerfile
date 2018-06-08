FROM openjdk:jre-alpine  
MAINTAINER Ross Allan <docker@nallar.me>  
  
ENV LANG=C.UTF-8 \  
FIXPERMISSIONS=true \  
LOGPATH=/log \  
LOGFILE=access.log \  
REPORTPATH=/report \  
REPORTFILE=index.html \  
REALTIMEREPORTFILE=realtime.html \  
REALTIMEENABLED=false \  
CONFIGPATH=/config \  
WSHOST=auto  
  
COPY root/ /  
RUN chmod +x /root/*.sh && /bin/sh /root/install.sh  
  
VOLUME /report /log /config  
  
ENTRYPOINT ["/sbin/tini", "-g", "-v", "--", "/root/init.sh"]  

