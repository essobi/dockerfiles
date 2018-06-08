FROM zurbaev/php71-dashboard  
MAINTAINER Timur Zurbaev <zurbaev@gmail.com>  
  
RUN DEBIAN_FRONTEND=noninteractive  
RUN locale-gen en_US.UTF-8  
  
ENV LANGUAGE=en_US.UTF-8  
ENV LC_ALL=en_US.UTF-8  
ENV LC_CTYPE=UTF-8  
ENV LANG=en_US.UTF-8  
ENV TERM xterm  
  
RUN apt-get update && \  
apt-get install -y supervisor  
  
ENTRYPOINT ["/usr/bin/supervisord", "-n", "-c",
"/etc/supervisor/supervisord.conf"]  

