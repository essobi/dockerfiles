FROM ubuntu:latest  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# install packages  
RUN apt-get update && apt-get install -y python imagemagick python-pip wget
vim  
  
RUN pip install azure  
  
COPY upload.py /upload.py  
  
COPY docker-entrypoint.sh /entrypoint.sh  
RUN chmod+x /entrypoint.sh  
  
CMD ["/entrypoint.sh"]  

