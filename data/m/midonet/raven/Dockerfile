FROM alpine  
MAINTAINER Antoni Segura Puimedon "toni@midokura.com"  
WORKDIR /  
RUN apk add --no-cache \  
python3 && \  
apk add --no-cache --virtual build-deps \  
gcc \  
git \  
linux-headers \  
musl-dev \  
python3-dev && \  
python3 -m ensurepip && \  
pip3 --no-cache-dir install --upgrade pip setuptools && \  
git clone https://github.com/midonet/kuryr.git -b k8s && \  
cd kuryr && \  
pip3 --no-cache-dir install --upgrade pip setuptools && \  
pip3 install . && \  
cd / && \  
rm -fr /raven && \  
apk del build-deps && \  
mkdir -p /var/log/raven && \  
addgroup kuryr -g 1000 && \  
adduser -u 1000 -D -s /bin/false -G kuryr kuryr  
  
ENV SERVICE_USER="admin"  
ENV SERVICE_TENANT_NAME="admin"  
ENV SERVICE_PASSWORD="admin"  
ENV IDENTITY_URL="http://127.0.0.1:35357/v2.0"  
ENV OS_URL="http://127.0.0.1:9696"  
ENV K8S_API="http://127.0.0.1:8080"  
ENV SERVICE_CLUSTER_IP_RANGE="10.0.0.0/24"  
USER kuryr  
  
CMD ["/usr/bin/raven"]  

