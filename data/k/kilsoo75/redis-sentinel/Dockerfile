FROM redis  
  
COPY redis-sentinel.conf /usr/local/etc/redis/redis-sentinel.conf  
  
RUN chown -R redis:redis /usr/local/etc/redis  
  
ENV MASTER_DEFAULT_PASSWORD redis1234  
  
# dns of redis-master  
ENV MASTER_DEFAULT_NAME redis-master  
  
# base tunning for redis  
RUN echo "vm.overcommit_memory = 1" >> /etc/sysctl.conf;  
#sysctl vm.overcommit_memory=1  
COPY docker-entrypoint.sh /usr/local/bin/  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 16379  
CMD [ "redis-server", "/usr/local/etc/redis/redis-sentinel.conf", "--sentinel"
]  

