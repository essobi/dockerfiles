FROM davidverdejo/alpine-opencv-microimage  
  
MAINTAINER David Verdejo <david.verdejo@bluekiri.com>  
  
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories && \  
apk update && \  
apk upgrade && \  
apk add --update --no-cache \  
# for build  
build-base \  
clang-dev \  
# for healthcheck  
curl \  
# for thumbor  
curl-dev \  
#zlib-dev \  
jpeg-dev \  
openssl-dev && \  
pip install --use-wheel --no-cache-dir \  
envtpl==0.5.3 \  
pyremotecv==0.5.0 \  
remotecv==2.2.1 \  
opencv-engine==1.0.1 \  
#error png in 6.3.x - https://github.com/thumbor/thumbor/issues/943  
#thumbor==6.3.2  
thumbor==6.2.0 && \  
#http://thumbor.readthedocs.io/en/latest/plugins.html  
apk del \  
build-base \  
clang-dev \  
curl-dev && \  
#http://thumbor.readthedocs.io/en/latest/plugins.html  
rm -rf /var/cache/apk/* && \  
rm -rf /tmp/*  
  
ENV HOME /usr/src/app  
ENV SHELL bash  
ENV WORKON_HOME /usr/src/app  
WORKDIR /usr/src/app  
  
COPY conf/thumbor.conf.tpl /usr/src/app/thumbor.conf.tpl  
COPY docker-entrypoint.sh /  
  
HEALTHCHECK \--interval=5s --timeout=3s \  
CMD curl -f http://localhost:8000/healthcheck || exit 1  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["thumbor"]  
  
EXPOSE 8000  

