FROM alpine:3.6  
  
ARG S6_VERSION=1.21.2.1  
  
WORKDIR /srv/dataproxy  
  
COPY . .  
  
RUN apk add --update --no-cache \  
python && \  
python -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip install --upgrade pip setuptools && \  
apk add --update-cache \  
curl \  
git \  
nano \  
py-lxml && \  
pip -q install --upgrade \  
gunicorn \  
html5lib \  
json-table-schema && \  
mkdir -p /srv/config /etc/services.d/dataproxy && \  
cp docker/gunicorn_conf.py /srv/config && \  
cp docker/run_dataproxy /etc/services.d/dataproxy/run && \  
mkdir -p /var/log/dataproxy && \  
touch /var/log/dataproxy/dataproxy.access.log && \  
touch /var/log/dataproxy/dataproxy.error.log && \  
git submodule init dataproxy && \  
git submodule update dataproxy && \  
apk add --virtual .gevent-deps \  
build-base \  
python-dev && \  
pip install gevent && \  
apk del \  
.gevent-deps && \  
rm -r /root/.cache && \  
rm -rf /var/cache/apk/* && \  
curl -sL https://github.com/just-
containers/s6-overlay/releases/download/v${S6_VERSION}/s6-overlay-amd64.tar.gz
-o /tmp/s6.tgz && \  
tar xzf /tmp/s6.tgz -C / && \  
rm -f /tmp/s6.tgz  
  
EXPOSE 5000  
  
ENTRYPOINT ["/init"]  
  
CMD []  

