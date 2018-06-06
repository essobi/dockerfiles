FROM redis:alpine  
  
RUN mkdir /src  
WORKDIR /src  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apk add --update supervisor ruby ruby-dev redis && gem install --no-ri
--no-rdoc redis  
RUN apk add openssh-client  
  
ADD . /src/  
  
COPY redis-trib.rb /usr/bin/redis-trib.rb  
COPY start-redis.sh /bin/start-redis.sh  
COPY start-cluster.sh /bin/start-cluster.sh  
COPY join.sh /bin/join.sh  
COPY addHostToHaproxy.sh /bin/addHostToHaproxy.sh  
COPY id_rsa /root/.ssh/id_rsa  
ADD id_rsa /root/.ssh/id_rsa  
RUN chmod 700 /root/.ssh/id_rsa  
RUN chmod +x /bin/start-redis.sh  
RUN chmod +x /bin/start-cluster.sh  
RUN chmod +x /bin/join.sh  
RUN chmod +x /bin/addHostToHaproxy.sh  
  
VOLUME ["/data"]  
  
CMD . /bin/start-redis.sh  

