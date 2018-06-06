FROM python:2-alpine  
  
ENV DUMB_VERSION=1.2.0  
ADD https://github.com/Yelp/dumb-init/releases/download/v${DUMB_VERSION}/dumb-
init_${DUMB_VERSION}_amd64 /usr/bin/dumb-init  
  
ADD docker-entrypoint.sh /usr/bin/docker-entrypoint.sh  
ADD . /app  
  
WORKDIR /app  
  
RUN pip install -r requirements.txt && \  
chmod +x /usr/bin/dumb-init  
  
ENTRYPOINT ["/usr/bin/docker-entrypoint.sh"]  

