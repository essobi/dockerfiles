FROM gliderlabs/alpine:3.1  
MAINTAINER jiri.fabian@topmonks.com  
  
ENV CONFIG_PATH="/home/Ogar/src"  
ADD files/docker-entrypoint.sh /docker-entrypoint.sh  
  
RUN chmod 755 /docker-entrypoint.sh && \  
apk --update add bash nodejs git && \  
mkdir -p /home && \  
cd /home && \  
git clone git://github.com/forairan/Ogar.git Ogar && \  
npm install ws  
  
ADD files/botnames.txt /home/Ogar/src/  
ADD files/gameserver.ini /home/Ogar/src/  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

