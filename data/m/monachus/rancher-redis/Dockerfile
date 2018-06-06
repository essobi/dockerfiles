FROM redis:3.2.0  
RUN apt-get -qq -y update && \  
apt-get -qq install curl sed wget && \  
rm -fr /var/lib/apt/lists/*  
  
# Install [dumb-init](https://github.com/Yelp/dumb-init)  
ENV DI_VERSION 1.2.0  
RUN cd /tmp && \  
wget -q -O /bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v${DI_VERSION}/dumb-init_${DI_VERSION}_amd64 && \  
chmod +x /bin/dumb-init  
  
ENV V_GIDDYUP 0.17.1  
RUN wget -q -O /usr/local/bin/giddyup
https://github.com/rancher/giddyup/releases/download/v${V_GIDDYUP}/giddyup &&
\  
chmod 755 /usr/local/bin/giddyup  
  
COPY conf/redis.conf /usr/local/etc/redis/redis.conf  
COPY start-redis.sh /start-redis.sh  
RUN chmod 755 /start-redis.sh  
  
ENTRYPOINT ["/bin/dumb-init", "--"]  
CMD ["/start-redis.sh"]  

