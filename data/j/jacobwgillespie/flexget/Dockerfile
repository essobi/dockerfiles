FROM python:2-onbuild  
  
RUN \  
# Create abc user  
groupmod -g 1000 users && \  
useradd -u 911 -U -d /config -s /bin/false abc && \  
usermod -G users abc  
  
VOLUME ["/config"]  
  
WORKDIR /config  
  
ADD files/start.sh /tmp/  
  
CMD /tmp/start.sh  

