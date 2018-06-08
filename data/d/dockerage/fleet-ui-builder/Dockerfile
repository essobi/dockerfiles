FROM google/golang:1.4  
MAINTAINER dockerage <dockerage@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install build-essential, ruby, and nodejs, etc.  
# Also install docker.io, which necessary only  
# when host os is not same as the base image of this Dockerfile  
RUN echo 'deb http://http.debian.net/debian wheezy-backports main' >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install --force-yes -y apt-utils ruby-full build-essential rubygems
\  
&& apt-get install --force-yes -y -t wheezy-backports linux-image-amd64 nodejs
libpng-dev \  
&& update-alternatives --install /usr/bin/node nodejs /usr/bin/nodejs 100 \  
&& curl -sSL https://get.docker.com/ | sh \  
&& curl -L https://www.npmjs.org/install.sh | sh \  
&& gem install compass rdoc  
  
RUN npm install -g angular \  
&& npm install -g grunt-cli \  
&& npm install -g bower  
  
ADD compile-build.sh /root/compile-build.sh  
RUN chmod 755 /root/compile-build.sh  
  
# Expose ${GOPATH}/src/  
VOLUME ${GOPATH}/src/  
  
WORKDIR /root  
CMD ./compile-build.sh  

