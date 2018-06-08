FROM ubuntu:14.04  
MAINTAINER kelu <kelostrada@gmail.com>  
  
# Install wget  
RUN apt-get update \  
&& apt-get install -y wget \  
&& apt-get autoremove -y \  
&& apt-get clean -y \  
&& apt-get autoclean -y \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install litecoind  
ENV VERSION 0.10.4.0  
WORKDIR /opt/litecoind  
RUN wget
https://download.litecoin.org/litecoin-$VERSION/linux/litecoin-$VERSION-
linux64.tar.gz \  
&& tar zxvf litecoin-$VERSION-linux64.tar.gz \  
&& ln -sfv /opt/litecoind/litecoin-$VERSION/bin/* /usr/local/bin \  
&& rm -rf litecoin-$VERSION-linux64.tar.gz  
  
# Add user litecoin  
ENV HOME /litecoin  
RUN useradd -s /bin/bash -m -d /litecoin litecoin  
RUN chown litecoin:litecoin -R /litecoin  
  
# Copy scripts  
COPY ./bin/* /usr/local/bin/  
RUN chmod a+x /usr/local/bin/*  
  
# For some reason, docker.io (0.9.1~dfsg1-2) pkg in Ubuntu 14.04 has
permission  
# denied issues when executing /bin/bash from trusted builds. Building locally  
# works fine (strange). Using the upstream docker (0.11.1) pkg from  
# http://get.docker.io/ubuntu works fine also and seems simpler.  
USER litecoin  
  
VOLUME ["/litecoin"]  
  
EXPOSE 9332 9333 19332 19333  
WORKDIR /litecoin  
  
CMD ["ltc_oneshot"]  
  

