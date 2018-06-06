# based on https://github.com/arnishow/clamav  
FROM meedan/base  
  
MAINTAINER sysops@meedan.com  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
clamav \  
clamav-daemon  
  
COPY freshclam.conf /etc/clamav/freshclam.conf  
RUN mkdir /run/clamav && chown clamav:clamav /run/clamav  
  
RUN freshclam --show-progress  
  
COPY entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
  
COPY clamd.conf /etc/clamav/clamd.conf  
  
EXPOSE 3310/tcp  
ENTRYPOINT ["/entrypoint.sh"]  

