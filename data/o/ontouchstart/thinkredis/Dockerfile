FROM ontouchstart/thinkredis:unstable  
RUN redis-server --version  
RUN redis-cli --version  
RUN cd / && git clone https://github.com/antirez/neural-redis.git  
RUN cd /neural-redis && git log -1 && make  
RUN echo 'loadmodule /neural-redis/neuralredis.so' > /etc/redis.conf  
WORKDIR /home  

