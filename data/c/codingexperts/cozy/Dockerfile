FROM debian:jessie  
  
RUN apt-get update && apt-get --no-install-recommends -y install \  
git \  
ca-certificates \  
curl \  
net-tools \  
nginx \  
sudo \  
vim-tiny \  
build-essential \  
pkg-config \  
erlang \  
libicu-dev \  
libmozjs185-dev \  
libcurl4-openssl-dev  
  
  
# Cozy-stack  
RUN cd /tmp && \  
curl -LO https://storage.googleapis.com/golang/go1.8.3.linux-amd64.tar.gz && \  
tar -C /usr/local -xzf go1.8.3.linux-amd64.tar.gz && \  
GOPATH=/tmp && \  
PATH=$PATH:/usr/local/go/bin go get -u github.com/cozy/cozy-stack && \  
cp /root/go/bin/cozy-stack /usr/local/bin/cozy-stack && \  
chmod +x /usr/local/bin/cozy-stack && \  
adduser --system \  
\--no-create-home \  
\--shell /bin/bash \  
\--group --gecos \  
"Cozy" cozy && \  
# @FIXME we should remove this hack and use `--fs-url
file://localhost/var/lib/cozy` once its available  
mkdir /usr/local/bin/storage && \  
chown cozy: /usr/local/bin/storage && \  
mkdir /var/log/cozy && \  
chown cozy: /var/log/cozy && \  
mkdir /var/lib/cozy && \  
chown -R cozy: /var/lib/cozy && \  
mkdir /etc/cozy && \  
curl -o /etc/cozy/cozy.yaml https://raw.githubusercontent.com/cozy/cozy-
stack/master/cozy.example.yaml && \  
chown -R cozy: /etc/cozy  
  
COPY ./start.sh /  
COPY ./nginx-config /etc/cozy/  
  
RUN chmod +x /start.sh  
  
EXPOSE 8080 6060 5984 443  
  
ENTRYPOINT ["/start.sh"]  

