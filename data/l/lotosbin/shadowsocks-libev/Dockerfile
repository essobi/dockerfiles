FROM ubuntu:16.04  
  
MAINTAINER lotosbin <lotosbin@gmail.com>  
  
ENV DEPENDENCIES git-core build-essential autoconf libtool libssl-dev libpcre3
libpcre3-dev asciidoc  
ENV DEV_DEPENDENCIES git-core build-essential autoconf libtool libssl-dev  
ENV BASEDIR /tmp/shadowsocks-libev  
ENV PORT 8338  
ENV VERSION v2.5.6  
  
RUN apt-get update  
RUN apt-get install -y shadowsocks  
# Set up building environment  
# ADD ./install2.sh /tmp/  
# RUN /tmp/install2.sh  
# RUN apt-get update \  
# && apt-get install --no- -y $DEPENDENCIES  
  
# Get the latest code, build and install  
# RUN git clone https://github.com/shadowsocks/shadowsocks-libev.git $BASEDIR  
# WORKDIR $BASEDIR  
# RUN git checkout $VERSION \  
# && ./configure \  
# && make \  
# && make install  
  
# Tear down building environment and delete git repository  
WORKDIR /  
#RUN rm -rf $BASEDIR/shadowsocks-libev \  
# && apt-get --purge autoremove -y $DEPENDENCIES  
  
# Port in the json config file won't take affect. Instead we'll use 8388.  
EXPOSE $PORT  
  
ADD ./start.sh /start.sh  
ENTRYPOINT ["/start.sh"]  
# Override the host and port in the config file.  
# ADD entrypoint /  
# ENTRYPOINT ["/entrypoint"]  
# CMD ["-h"]  

