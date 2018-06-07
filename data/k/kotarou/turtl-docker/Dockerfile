FROM ubuntu:16.04  
ENV CCL_VERSION 1.11  
ENV DEBIAN_FRONTEND noninteractive  
  
ADD https://download.rethinkdb.com/apt/pubkey.gpg /tmp/rethinkdb-pubkey.gpg  
ADD https://nginx.org/keys/nginx_signing.key /tmp/nginx.key  
  
RUN echo "deb http://download.rethinkdb.com/apt xenial main" | tee
/etc/apt/sources.list.d/rethinkdb.list && \  
echo "deb http://nginx.org/packages/mainline/ubuntu/ xenial nginx" | tee
/etc/apt/sources.list.d/nginx && \  
apt-key add - < /tmp/nginx.key && \  
apt-key add - < /tmp/rethinkdb-pubkey.gpg && \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y curl wget \  
libterm-readline-perl-perl \  
gcc \  
libuv1-dev \  
git \  
rethinkdb \  
sendmail \  
nginx && \  
curl -sL https://deb.nodesource.com/setup_8.x | bash - && \  
apt-get install -y nodejs build-essential  
  
# nginx for turtl web  
ADD turtl.nginx.conf /etc/nginx/sites-aviable/turtl.conf  
RUN ln -s /etc/nginx/sites-aviable/turtl.conf /etc/nginx/sites-
enabled/turtl.conf && \  
rm /etc/nginx/sites-enabled/default && \  
mkdir /opt/turtl && \  
mkdir /etc/nginx/external  
  
# turtl web  
RUN cd /opt/turtl && \  
git clone https://github.com/turtl/js && \  
cd js && \  
cat config/config.js.default | sed "s/http:\/\/turtl.dev:8181/\/api/" >
config/config.js && \  
npm install && \  
make  
  
# Install ccl  
RUN wget -P /opt/
ftp://ftp.clozure.com/pub/release/${CCL_VERSION}/ccl-${CCL_VERSION}-linuxx86.tar.gz
&& \  
mkdir -p /opt/ccl && \  
tar xvzf /opt/ccl-${CCL_VERSION}-linuxx86.tar.gz -C /opt/ccl --strip-
components=1  
  
# install quicklisp  
COPY quicklisp_install /quicklisp_install  
RUN wget https://beta.quicklisp.org/quicklisp.lisp  
RUN cat /quicklisp_install | /opt/ccl/lx86cl64 --load /quicklisp.lisp  
  
# install turtl API  
RUN cd /opt/ && \  
git clone https://github.com/turtl/api.git --depth 1  
RUN cd /root/quicklisp/local-projects && \  
git clone git://github.com/orthecreedence/cl-hash-util  
RUN /opt/ccl/lx86cl64 -l /root/quicklisp/setup.lisp  
  
# config  
COPY config.footer /opt/api/config/  
COPY turtl-setup /opt/  
COPY turtl-start /opt/  
RUN chmod a+x /opt/turtl-setup  
RUN chmod a+x /opt/turtl-start  
COPY launch.lisp /opt/api/  
COPY rethinkdb.conf /etc/rethinkdb/instances.d/instance1.conf  
  
# general settings  
EXPOSE 80  
WORKDIR /opt/api  
VOLUME /var/lib/rethinkdb/instance1  
VOLUME /opt/api/uploads  
CMD /opt/turtl-setup  
  
# clean  
RUN apt-get purge -y build-essential curl wget && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  

