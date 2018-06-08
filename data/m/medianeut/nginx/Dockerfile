# Use Alpine Linux  
FROM alpine:3.3  
# Env  
ENV ROOT /data  
ENV TIMEZONE=Europe/Brussels \  
CONF_SRC=./conf \  
CONF_DIR=/tmp/conf \  
SCRIPTS_SRC=./scripts \  
SCRIPTS_DIR=${ROOT}/scripts  
  
# Let's roll  
RUN apk update && \  
apk upgrade && \  
apk add --update openssl nginx bash py-pip && \  
apk add --update tzdata && \  
pip install -U Jinja2 && \  
cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && \  
echo "${TIMEZONE}" > /etc/timezone && \  
mkdir /etc/nginx/certificates && \  
openssl req \  
-x509 \  
-newkey rsa:2048 \  
-keyout /etc/nginx/certificates/key.pem \  
-out /etc/nginx/certificates/cert.pem \  
-days 365 \  
-nodes \  
-subj /CN=localhost && \  
mkdir /www && \  
apk del tzdata && \  
rm -rf /var/cache/apk/*  
  
# COPY etc/nginx.conf /etc/nginx/nginx.conf  
# COPY etc/common.conf /etc/nginx/common.conf  
# COPY etc/conf.d/default.conf /etc/nginx/conf.d/default.conf  
# COPY etc/conf.d/ssl.conf /etc/nginx/conf.d/ssl.conf  
ADD ${CONF_SRC} ${CONF_DIR}  
ADD ${SCRIPTS_SRC} ${SCRIPTS_DIR}  
ADD ./etc/nginx /etc/nginx  
  
# Expose ports  
EXPOSE 80 443  
# Entry point  
ENTRYPOINT ${SCRIPTS_DIR}/run.sh  

