FROM ubuntu:latest  
MAINTAINER Philipp Göllner <philipp@goellner.it>  
  
RUN apt-get update && apt-get install -y \  
rsync ssh cifs-utils  
  
ENV RUN_USER root  
  
  
ENV BACKUP_HOST false  
ENV BACKUP_PATH false  
ENV BACKUP_USER false  
ENV BACKUP_SSHKEY false  
  
VOLUME /source  
  
USER ${RUN_USER}  
  
COPY configure-and-start.sh /  
WORKDIR /  
  
CMD ["/configure-and-start.sh", "-fg"]

