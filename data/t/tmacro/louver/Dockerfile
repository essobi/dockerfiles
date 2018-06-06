FROM justcontainers/base-alpine:latest  
MAINTAINER Taylor McKinnon <taylor@uncannypacket.com>  
  
## Set some config options  
ENV DOCKER_GEN_VER 0.7.3  
ENV HOST_DOCKER unix:///var/run/docker.sock  
ENV PROXY_HTTPS=false PROXY_HTTPS_REDIRECT=false  
ENV ETCD_ROOT /services  
ENV OP_MODE cluster  
  
## Install required software  
RUN apk-install haproxy python3 git  
RUN python3 -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip3 install --upgrade pip setuptools  
  
# Install fixed python-etcd  
RUN git clone https://github.com/tmacro/python-etcd.git /tmp/python-etcd && \  
cd /tmp/python-etcd && \  
python3 setup.py install  
  
# Install dockergen  
ADD https://github.com/jwilder/docker-
gen/releases/download/$DOCKER_GEN_VER/docker-gen-alpine-linux-
amd64-$DOCKER_GEN_VER.tar.gz /tmp/docker-gen.tar.gz  
RUN tar xvzf /tmp/docker-gen.tar.gz -C /usr/local/bin  
# Install required modules  
ADD ./requirements.txt /tmp/  
RUN pip3 install -r /tmp/requirements.txt && rm /tmp/requirements.txt  
  
RUN touch /var/run/haproxy.pid && mkdir -p /run/nginx  
  
ADD ./configure-services /etc/cont-init.d/  
ADD ./s6 /etc/services.d  
  
# And finally install the app  
ADD . /app  
  
EXPOSE 1936 80  

