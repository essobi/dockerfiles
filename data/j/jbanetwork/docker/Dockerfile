FROM alpine:3.6  
  
ENV DOCKER_COMPOSE_VERSION 1.16.1  
  
RUN echo "@edgecommunity http://nl.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories && \  
apk add --update --no-cache \  
build-base \  
python3 \  
python3-dev \  
libseccomp \  
libffi-dev \  
openssl-dev \  
docker@edgecommunity \  
bash \  
git \  
&& \  
apk add --no-cache --virtual=build-dependencies && \  
pip3 install docker-compose==${DOCKER_COMPOSE_VERSION} && \  
apk del build-base build-dependencies python3-dev && \  
rm -r /root/.cache  
  
CMD ["bash"]  

