# docker build  
# docker build -t purpleworks/fleet-ui .  
#  
# docker run  
# docker run --rm -p [port]:3000 -e ETCD_PEER=[your_etcd_peer_ip] -v
[your_ssh_private_key_file_path]:/root/id_rsa purpleworks/fleet-ui  
# docker run --rm -p 3000:3000 -e ETCD_PEER=10.0.0.1 -v
~/.ssh/id_rsa:/root/id_rsa purpleworks/fleet-ui  
FROM google/golang:1.4  
MAINTAINER Xu Wang <xuwang@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install build-essential, ruby, and nodejs, etc.  
# Also install docker.io, which necessary only.  
# when host os is not same as the base image of this Dockerfile  
RUN echo 'deb http://http.debian.net/debian wheezy-backports main' >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install --force-yes -y apt-utils ruby-full build-essential rubygems
openssh-client \  
&& apt-get install --force-yes -y -t wheezy-backports linux-image-amd64 nodejs
libpng-dev \  
&& update-alternatives --install /usr/bin/node nodejs /usr/bin/nodejs 100 \  
&& curl -sSL https://get.docker.com/ | sh \  
&& curl -L https://www.npmjs.org/install.sh | sh \  
&& gem install compass rdoc  
  
RUN npm install -g angular \  
&& npm install -g grunt-cli \  
&& npm install -g bower  
  
ENV APPDIR /gopath/src/github.com/fleet-ui  
  
# Compile angular  
COPY angular $APPDIR/angular  
WORKDIR $APPDIR/angular  
RUN npm install  
RUN bower install --allow-root  
RUN grunt build --force  
RUN mv dist ../public/  
  
# Compile go app  
COPY . $APPDIR  
WORKDIR $APPDIR  
RUN go get && go install  
  
# add fleet-ui  
RUN cp $GOPATH/bin/fleet-ui $APPDIR/fleet-ui  
  
# add fleet  
ENV FLEET_VERSION 0.10.2  
RUN curl -s -L
https://github.com/coreos/fleet/releases/download/v${FLEET_VERSION}/fleet-v${FLEET_VERSION}-linux-
amd64.tar.gz \  
| tar xz fleet-v${FLEET_VERSION}-linux-amd64/fleetctl -O >
/usr/local/bin/fleetctl \  
&& chmod +x /usr/local/bin/fleetctl  
  
# export port  
EXPOSE 3000  
# run!  
CMD ./run.sh  

