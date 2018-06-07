FROM debian:stretch  
MAINTAINER Louis Fradin <louis.fradin@gmail.com>  
  
# Installs  
RUN apt-get update && \  
apt-get install lftp cron -y  
  
# Volumes  
VOLUME /sync  
  
# Envirnment variables  
ENV BOX_PASSWORD ""  
ENV BOX_USERNAME ""  
ENV SYNC_DIR /sync  
ENV DISTANT_DIR ""  
ENV UNTRUSTED_CERTIFICATE no  
ENV PERIODIC_SYNC "no"  
ENV CRON_SCHEME "* * * * *"  
# Files  
COPY . /box-ftp-sync/  
  
# Command  
CMD [ "bash", "/box-ftp-sync/docker/entrypoint.sh" ]  

