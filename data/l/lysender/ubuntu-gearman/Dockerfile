FROM ubuntu:wily  
MAINTAINER Leonel Baer <leonel@lysender.com>  
  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get -y install git \  
supervisor \  
gearman-job-server \  
libgearman7 \  
libgearman-dev && apt-get clean  
  
# Configure servicies  
ADD ./start.sh /start.sh  
RUN chmod 755 /*.sh  
RUN mkdir -p /etc/supervisor/conf.d  
ADD ./supervisor-gearmand.conf /etc/supervisor/conf.d/gearmand.conf  
  
RUN mkdir -p /var/log/gearmand  
  
VOLUME ["/var/log/gearmand"]  
  
EXPOSE 4730  
CMD ["/bin/bash", "/start.sh"]  

