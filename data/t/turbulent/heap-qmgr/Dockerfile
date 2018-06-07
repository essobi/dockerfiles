FROM turbulent/heap-app:5.0.1  
MAINTAINER Benoit Beausejour <b@turbulent.ca>  
  
ENV heap-qmgr 6.0.0  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get -y install -y imagemagick \  
ghostscript \  
libreoffice \  
pdftk && \  
rm -rf /var/lib/apt/lists/*  
  
ADD supervisord.conf.tmpl /systpl/supervisord.conf.tmpl  
ADD run-heap-qmgr.sh.tmpl /systpl/run-heap-qmgr.sh.tmpl  
ADD run.sh /run.sh  
  
ENV VAR_HEAP_QUEUE_WORKERS=2 \  
VAR_HEAP_QUEUE_NAME="media"  
VOLUME ["/vol/website"]  
  
CMD ["/run.sh"]  
ENTRYPOINT []  

