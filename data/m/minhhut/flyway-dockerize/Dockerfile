FROM boxfuse/flyway:latest-alpine  
  
WORKDIR /flyway  
  
ENV DOCKERIZE_VERSION v0.5.0  
RUN apk --no-cache add openssl \  
&& wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
\  
&& rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
ENTRYPOINT ["flyway"]  
CMD ["-?"]  

