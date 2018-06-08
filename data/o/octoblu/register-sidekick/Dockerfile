FROM mailgun/vulcand:v0.8.0-beta.3  
MAINTAINER Octoblu Inc. <docker@octoblu.com>  
  
RUN apt-get update && apt-get install -y jq && rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
COPY register-healthcheck.sh /usr/src/app/  
COPY run.sh /usr/src/app/  
  
CMD ["./run.sh"]  

