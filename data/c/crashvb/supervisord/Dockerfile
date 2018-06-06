FROM crashvb/base:ubuntu  
LABEL maintainer="Richard Davis <crashvb@gmail.com>"  
  
# Install packages, download files ...  
RUN docker-apt supervisor  
  
# Configure: supervisor  
ADD supervisord.conf /etc/supervisor/conf.d/10supervisord.conf  
  
# Configure: healthcheck  
ADD healthcheck.supervisord /etc/healthcheck.d/supervisord  
  
CMD ["/usr/bin/supervisord", "--
configuration=/etc/supervisor/supervisord.conf"]  

