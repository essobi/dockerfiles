FROM haproxy:1.5  
RUN apt-get update && apt-get install -y inotify-tools  
  
RUN mkdir -p /var/lib/haproxy  
RUN mkdir -p /run/haproxy  
  
COPY ./init.sh /bin/init  

