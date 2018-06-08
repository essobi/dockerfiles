# ---- Atigeobase-Dockerfile ------------------------------  
# ---- Version control ------------------------------------  
FROM ubuntu:14.04.5  
ENV OPENSSL_VERSION openssl-1.0.2j  
ENV OPENSSL_DOWNLOAD_LINK
https://www.openssl.org/source/$OPENSSL_VERSION.tar.gz  
  
  
# ---- apt-get --------------------------------------------  
RUN apt-get update && \  
#apt-get upgrade -y && \  
apt-get install -y --no-install-recommends \  
build-essential \  
ca-certificates \  
curl \  
wget \  
net-tools \  
vim && \  
# installed as part of ca-certificates  
update-ca-certificates && \  
rm -rf /var/lib/apt/lists/*  
  
  
# ---- Set the locale -------------------------------------  
RUN locale-gen en_US.UTF-8 && \  
update-locale LANG=en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# ---- Update OpenSSL -------------------------------------  
RUN wget $OPENSSL_DOWNLOAD_LINK -P /tmp/ && \  
tar xzf /tmp/$OPENSSL_VERSION.tar.gz -C /tmp/ && \  
cd /tmp/$OPENSSL_VERSION && \  
./config --prefix=/usr/ && \  
make && \  
make install && \  
rm -Rf /tmp/*  

