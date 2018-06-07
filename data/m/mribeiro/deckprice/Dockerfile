FROM debian:stable  
MAINTAINER Marcio Ribeiro <binary@b1n.org>  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm-color  
  
RUN apt-get update -q && apt-get install -qy php5-cli  
  
COPY price.php /usr/bin/price.php  
COPY run_price.sh /usr/bin/run_price.sh  
  
WORKDIR /data  
VOLUME ["/data"]  
  
ENTRYPOINT ["/usr/bin/run_price.sh"]  

