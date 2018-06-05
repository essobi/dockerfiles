FROM haproxy:1.6  
# install aws cli  
RUN apt-get update && apt-get install -y curl python-pip --no-install-
recommends && rm -rf /var/lib/apt/lists/*  
RUN pip install awscli  
  
#Override the original docker-entrypoint  
COPY docker-entrypoint.sh /  
COPY build-config /  
COPY haproxy.template /usr/local/etc/haproxy/haproxy.template  
EXPOSE 3306 8080  
RUN chmod +x /docker-entrypoint.sh /build-config

