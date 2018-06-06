FROM redis:3.2.8  
ENV DOCKERIZE_VERSION v0.4.0  
COPY bin/run.sh /usr/local/bin/run.sh  
  
RUN apt-get update && apt-get install -y wget \  
&& wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
\  
&& rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& chmod +x /usr/local/bin/run.sh \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY config/ /redis/config  
  
CMD ["/usr/local/bin/run.sh"]

