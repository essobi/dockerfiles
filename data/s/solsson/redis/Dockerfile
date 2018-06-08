FROM redis:3.0.7  
MAINTAINER Michal Balinski <michal.balinski@gmail.com>  
  
COPY ./entrypoint.sh /entrypoint.sh  
RUN chown redis:redis /entrypoint.sh && \  
chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]

