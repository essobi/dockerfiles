FROM travix/base-alpine:3.5  
MAINTAINER Travix  
  
# build time environment variables  
ENV HAPROXY_VERSION=1.6.9-r1  
  
# install haproxy  
RUN apk --update --no-cache add \  
haproxy=$HAPROXY_VERSION \  
&& rm /var/cache/apk/*  
  
# copy configuration  
COPY entrypoint.sh /entrypoint.sh  
COPY haproxy.cfg /etc/haproxy/haproxy.cfg  
COPY ssl.pem /etc/ssl/private/ssl.pem  
  
# make entrypoint executable  
RUN chmod 500 /entrypoint.sh  
  
# expose ports  
EXPOSE 80 81 82 83 443  
# Define working directory  
WORKDIR /etc/haproxy  
  
# runtime environment variables  
ENV BASIC_AUTH="" \  
CLIENT_TIMEOUT="50000" \  
DIRECT_HOST_NAME="directhostname" \  
HEALT_CHECK_PATH="/healthz" \  
HEALT_CHECK_VERB="HEAD" \  
OFFLOAD_TO_HOST="localhost" \  
OFFLOAD_TO_PORT="5000" \  
SERVER_TIMEOUT="50000" \  
SSL_CERTIFICATE_NAME="ssl.pem" \  
STATS_PASSWORD="" \  
STATS_REFRESH_INTERVAL="5s" \  
TLS_SETTINGS="no-sslv3 no-tls-tickets force-tlsv12" \  
WHITELIST_CIDRS="0.0.0.0/0" \  
X_FORWARDED_FOR_HEADER="X-Forwarded-For" \  
X_FRAME_OPTIONS="DENY"  
ENTRYPOINT ["/entrypoint.sh"]  
  
# replace configuration value from environment variable and define default
command  
CMD ["haproxy", "-db", "-f", "/etc/haproxy/haproxy.cfg"]  

