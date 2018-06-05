FROM alpine:3.7  
  
ENV PROJECT_DIR /opt/calyx  
  
COPY src/ ${PROJECT_DIR}  
  
WORKDIR ${PROJECT_DIR}  
  
RUN apk update && \  
apk add --no-cache \  
mariadb-dev \  
pcre-dev \  
python3 && \  
apk add --no-cache --virtual=build_dep \  
python3-dev \  
gcc \  
build-base \  
linux-headers \  
tzdata && \  
pip3 install -r requirements.txt && \  
cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \  
apk del --purge build_dep && \  
rm /usr/lib/libmysqld* && \  
rm -rf /var/cache/apk/*  
  
CMD ["/usr/bin/uwsgi", "--ini", "uwsgi.ini"]

