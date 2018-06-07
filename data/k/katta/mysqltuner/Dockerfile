FROM debian:jessie  
MAINTAINER Andrea Cattaneo <andrea.cattaneo.dev@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -qq \  
&& apt-get install -y mysql-client perl curl \  
&& apt-get clean autoclean \  
&& apt-get autoremove --yes \  
&& rm -rf /var/lib/{apt/list,dpkg,cache,log}/*  
  
# install mysqltuner  
RUN curl -sL -o /usr/local/bin/mysqltuner http://mysqltuner.pl && \  
chmod +x /usr/local/bin/mysqltuner  
  
ADD mysqltuner_auto.sh /usr/local/bin/mysqltuner_auto  
RUN chmod +x /usr/local/bin/mysqltuner_auto  
  
VOLUME ["/data"]  
  
WORKDIR /data  
  
ENTRYPOINT ["/usr/local/bin/mysqltuner_auto"]  

