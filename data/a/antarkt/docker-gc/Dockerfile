FROM gliderlabs/alpine:3.3  
ENV DOCKER_VERSION 1.9.1  
# We get curl so that we can avoid a separate ADD to fetch the Docker binary,
and then we'll remove it  
RUN apk --update add bash curl \  
&& curl -s https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VERSION}
> /bin/docker \  
&& chmod +x /bin/docker \  
&& apk del curl \  
&& rm -rf /var/cache/apk/*  
  
COPY ./docker-gc /usr/sbin/docker-gc  
COPY ./entrypoint.sh /  
COPY cron/wrapper-docker-gc.sh /bin/wrapper-docker-gc  
  
RUN chmod +x /bin/wrapper-docker-gc && chmod +x /entrypoint.sh  
  
VOLUME /var/lib/docker-gc  
  
CMD ["/entrypoint.sh"]  

