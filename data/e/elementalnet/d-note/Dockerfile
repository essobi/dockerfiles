FROM alpine:3.5  
MAINTAINER Jan Kunzmann <jan-docker@phobia.de>  
  
RUN apk add --no-cache python2 py2-flask py2-crypto py-setuptools uwsgi uwsgi-
python git \  
&& git clone \--branch master --depth 1 https://github.com/elemental-
lf/d-note.git /build \  
&& cd /build \  
&& python setup.py install \  
&& cd / \  
&& rm -rf build \  
&& apk del git  
  
ENV GO_CRON_VERSION v0.0.7  
ADD https://github.com/odise/go-cron/releases/download/$GO_CRON_VERSION/go-
cron-linux.gz /  
RUN gunzip go-cron-linux.gz && chmod a+x /go-cron-linux  
  
COPY config/d-note.ini /etc/dnote/  
COPY script/uwsgi-http-dnote.sh /usr/local/bin/  
  
ENV APPLICATION_ROOT=/  
ENV PROCESSES=1  
ENV THREADS=2  
VOLUME /dnote  
EXPOSE 8080  
CMD [ "/usr/local/bin/uwsgi-http-dnote.sh" ]  

