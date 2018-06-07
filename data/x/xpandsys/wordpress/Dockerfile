FROM fkconsultin/docker-restyfpm:5.5  
MAINTAINER Florian Kasper <florian.kasper@xpandmmi.com>  
  
  
ENV WORDPRESS_VERSION 4.3  
ENV WORDPRESS_SHA1 1e9046b584d4eaebac9e1f7292ca7003bfc8ffd7  
  
COPY 00-install.sh /install  
RUN /install && rm /install  
  
COPY 01-run.sh /run.sh  
  
WORKDIR /system/wordpress  
  
CMD ["/run.sh"]  
  

