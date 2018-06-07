FROM boritzio/docker-base  
  
RUN apt-get install -y haproxy  
  
ADD https://raw.githubusercontent.com/mesosphere/marathon/master/bin/haproxy-
marathon-bridge scripts/  
  
RUN chmod +x scripts/haproxy-marathon-bridge  
  
ADD start.sh /etc/my_init.d/  

