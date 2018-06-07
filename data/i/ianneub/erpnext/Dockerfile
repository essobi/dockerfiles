FROM alpine:latest  
MAINTAINER Ian Neubert <ian@ianneubert.com>  
  
# Update  
ENV BRANCH=master \  
FRAPPE_USER=frappe \  
ERPNEXT_BRANCH=master  
  
RUN apk add --update \  
alpine-sdk \  
linux-headers \  
py-pip \  
python-dev \  
mariadb-client \  
mariadb-dev \  
zlib-dev \  
jpeg-dev \  
libffi-dev \  
xvfb \  
ttf-freefont \  
fontconfig \  
dbus \  
nodejs && \  
apk add wkhtmltopdf --update-cache \  
\--repository http://dl-3.alpinelinux.org/alpine/edge/testing/ \  
\--allow-untrusted && \  
mv /usr/bin/wkhtmltopdf /usr/bin/wkhtmltopdf-origin && \  
rm -rf /var/cache/apk/* && \  
pip install --upgrade pip && \  
addgroup -S $FRAPPE_USER && \  
adduser -D -G $FRAPPE_USER $FRAPPE_USER && \  
echo 'frappe ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers  
  
USER $FRAPPE_USER  
WORKDIR /home/$FRAPPE_USER  
RUN git clone -b $BRANCH \--depth 1 https://github.com/$FRAPPE_USER/bench
bench-repo && \  
sudo pip install -e /home/$FRAPPE_USER/bench-repo --no-cache-dir && \  
mkdir -p frappe-bench && cd frappe-bench && \  
mkdir -p apps logs sites/localhost config && \  
bench setup env && \  
sudo bench setup sudoers $FRAPPE_USER && \  
bench setup socketio && \  
bench get-app frappe https://github.com/frappe/frappe --branch $BRANCH  
  
ENV DOCKERIZE_VERSION v0.2.0  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& sudo tar -C /usr/local/bin -xzvf dockerize-linux-
amd64-$DOCKERIZE_VERSION.tar.gz && rm *.tar.gz  
  
COPY ./config/ /tmp/config  
COPY ./docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
COPY ./wkhtmltopdf /usr/bin/wkhtmltopdf  
RUN cp /tmp/config/apps.txt /home/$FRAPPE_USER/frappe-bench/sites/apps.txt &&
\  
sudo chmod +x /usr/local/bin/docker-entrypoint.sh  
  
ENV ADMIN_PASSWORD=frappe \  
DB_HOST=db \  
DB_NAME=frappe \  
DB_PASSWORD=frappe \  
DB_USER=frappe \  
MAIL_LOGIN= \  
MAIL_PASSWORD= \  
MAIL_PORT= \  
MAIL_SERVER= \  
REDIS_CACHE_URL=redis-cache \  
REDIS_QUEUE_URL=redis-queue \  
REDIS_SOCKETIO_URL=redis-socketio \  
ROOT_PASSWORD=root \  
USE_SSL=false \  
DEVELOPER_MODE=false  
  
WORKDIR /home/$FRAPPE_USER/frappe-bench  
RUN bench get-app erpnext https://github.com/frappe/erpnext --branch
$ERPNEXT_BRANCH  
  
VOLUME ["/home/$FRAPPE_USER/frappe-bench/logs", "/home/$FRAPPE_USER/frappe-
bench/sites/localhost", "/home/$FRAPPE_USER/frappe-bench/sites/assets",
"/home/$FRAPPE_USER/frappe-bench/apps/erpnext/erpnext/public",
"/home/$FRAPPE_USER/frappe-bench/apps/frappe/frappe/public"]  
  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
CMD ["app"]  

