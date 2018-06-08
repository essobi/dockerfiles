FROM debian:jessie  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV TYK_DOWNLOAD_URL
https://github.com/TykTechnologies/tyk/releases/download/v2.2/tyk-linux-
amd64-2.2.0.0.tar.gz  
ENV TYK_VERSION 2.2.0.0  
RUN wget -O tyk.tar.gz $TYK_DOWNLOAD_URL && \  
tar -xzf tyk.tar.gz && \  
mv tyk.linux.amd64-$TYK_VERSION /opt/tyk-gateway && \  
mv /opt/tyk-gateway/tyk /bin/tyk && \  
rm tyk.tar.gz && \  
rm -rf /opt/tyk-gateway/apps/* && \  
rm -rf /opt/tyk-gateway/policies/*  
  
ENV TYK_SECRET 352d20ee67be67f6340b4c0605b044b7  
  
ENV REDIS_HOST redis  
ENV REDIS_PORT 6379  
#ENV REDIS_PASSWORD test  
ENV USE_SENTRY false  
  
ENV API_NAME Tyk Test API  
ENV API_ID 1  
#ENV ORG_ID default  
ENV USE_KEYLESS false  
ENV AUTH_USE_PARAM false  
ENV AUTH_HEADER_NAME authorization  
ENV TARGET_URL http://httpbin.org  
ENV ENABLE_BATCH_REQUESTS true  
  
COPY app.json /opt/tyk-gateway/.docker/app.json  
COPY policies.json /opt/tyk-gateway/.docker/policies.json  
COPY tyk.conf /opt/tyk-gateway/.docker/tyk.conf  
COPY run.sh /opt/tyk-gateway/run.sh  
  
WORKDIR /opt/tyk-gateway  
  
EXPOSE 8080  
CMD ["./run.sh"]  

