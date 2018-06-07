FROM travix/base-alpine:latest  
  
MAINTAINER Travix  
  
# build time environment variables  
ENV USER_NAME=haproxy \  
USER_ID=999 \  
GROUP_NAME=haproxy \  
GROUP_ID=999  
# install haproxy  
RUN addgroup -S -g $GROUP_ID $GROUP_NAME \  
&& adduser -S -G $GROUP_NAME -u $USER_ID $USER_NAME \  
&& apk --update add \  
haproxy \  
&& rm /var/cache/apk/*  
  
ADD haproxy.cfg /etc/haproxy/haproxy.cfg  
ADD self-signed-certificate.pem /etc/ssl/private/self-signed-certificate.pem  
  
# expose ports  
EXPOSE 80 443  
# Define working directory  
WORKDIR /etc/haproxy  
  
# runtime environment variables  
ENV BACKEND_SERVER=localhost \  
BACKEND_SERVER_PORT=8080 \  
SSL_CERTIFICATE_NAME=self-signed-certificate.pem  
  
# define default command  
CMD deluser $USER_NAME; \  
delgroup $GROUP_NAME; \  
addgroup -S -g $GROUP_ID $GROUP_NAME; \  
adduser -S -G $GROUP_NAME -u $USER_ID $USER_NAME; \  
sed -i -e "s/localhost:8080/${BACKEND_SERVER}:${BACKEND_SERVER_PORT}/"
/etc/haproxy/haproxy.cfg; \  
sed -i -e "s/self-signed-certificate.pem/${SSL_CERTIFICATE_NAME}/"
/etc/haproxy/haproxy.cfg; \  
exec haproxy -db -f /etc/haproxy/haproxy.cfg;

