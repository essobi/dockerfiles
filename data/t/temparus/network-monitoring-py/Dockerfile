FROM alpine:3.5  
LABEL maintainer="Sandro Lutz <code@temparus.ch>"  
  
RUN apk add --no-cache python3 nmap nmap-nselibs nmap-scripts  
  
ADD . /network-monitoring.py/  
  
WORKDIR /network-monitoring.py  
  
RUN chmod 755 docker-entrypoint.sh docker-run.sh network-monitoring.py  
RUN touch /crontab.txt  
  
ENTRYPOINT ["./docker-entrypoint.sh"]

