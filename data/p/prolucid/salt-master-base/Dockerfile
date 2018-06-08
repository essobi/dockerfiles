FROM phusion/baseimage:0.9.19  
MAINTAINER Eugene Tolmachev  
ENV DEBIAN_FRONTEND noninteractive  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
ENV DISABLE_SSH 1  
ENV LOG_LEVEL debug  
ENV LOG_FILE_LEVEL debug  
ENV LOG_LOCATION /var/log/salt/master  
  
RUN apt-get update && apt-get install -yq --no-install-recommends wget  
  
RUN curl -o bootstrap_salt.sh -L https://bootstrap.saltstack.com && \  
# sh bootstrap_salt.sh -d -M -X git v2016.11.1  
sh bootstrap_salt.sh -d -M -X -g https://github.com/Prolucid/salt.git git
2016.11  
RUN apt-get update && apt-get install -yq --no-install-recommends \  
git \  
pkg-config \  
gcc build-essential cmake \  
python-setuptools python-dev python-pip \  
libffi-dev libssh-dev zlib1g-dev libssl-dev \  
libhttp-parser-dev virt-what \  
python-cherrypy3  
  
RUN pip install --upgrade pip && \  
cd /tmp && \  
wget https://github.com/openssl/openssl/archive/OpenSSL_1_1_0c.tar.gz && \  
tar xzf OpenSSL_1_1_0c.tar.gz && \  
cd openssl-OpenSSL_1_1_0c && \  
./config -fPIC --prefix=/usr/local/ -ldl && \  
make && \  
make install && \  
wget https://www.libssh2.org/download/libssh2-1.8.0.tar.gz && \  
tar xzf libssh2-1.8.0.tar.gz && \  
cd libssh2-1.8.0 && \  
./configure LIBS=-ldl --with-openssl --with-libz && \  
make && \  
make install && \  
cd /tmp && \  
wget https://github.com/libgit2/libgit2/archive/v0.25.1.tar.gz && \  
tar xzf v0.25.1.tar.gz && \  
cd libgit2-0.25.1/ && \  
cmake . && \  
make && \  
make install && \  
ldconfig && \  
pip install -I cffi && \  
pip install -I pygit2==0.25.0 && \  
pip install -I pyOpenSSL==16.2.0 && \  
cd /  
  
# Install Logstash  
RUN wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | apt-key add
-  
RUN echo "deb https://packages.elastic.co/logstash/2.3/debian stable main" |
tee -a /etc/apt/sources.list  
RUN apt-get update && apt-get install logstash  
  
# cleanup  
RUN apt-get purge gcc -yq && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Setup Service Startup Scripts  
RUN mkdir /etc/service/salt-master  
ADD salt-master.sh /etc/service/salt-master/run  
RUN chmod +x /etc/service/salt-master/run  
  
VOLUME ["/etc/salt"]  
EXPOSE 4505 4506 4430  

