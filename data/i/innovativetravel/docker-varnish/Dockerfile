# Varnish  
#  
# WEBSITE https://github.com/Zenedith/docker-varnish  
# VERSION 1.1.1  
FROM ubuntu  
MAINTAINER Mateusz Stępniak "zenedith@wp.pl"  
# make sure the package repository is up to date  
RUN apt-get update  
RUN apt-get install git pkg-config dpkg-dev autoconf curl make autotools-dev
automake libtool libpcre3-dev libncurses-dev python-docutils bsdmainutils
debhelper dh-apparmor gettext gettext-base groff-base html2text intltool-
debian libbsd-dev libbsd0 libcroco3 libedit-dev libedit2 libgettextpo0
libpipeline1 libunistring0 man-db po-debconf xsltproc libhiredis-dev -y  
  
# download repo key  
RUN curl -s http://repo.varnish-cache.org/debian/GPG-key.txt | apt-key add -  
RUN echo "deb http://repo.varnish-cache.org/ubuntu/ $(lsb_release -sc)
varnish-4.1" | tee -a /etc/apt/sources.list  
RUN echo "deb-src http://repo.varnish-cache.org/ubuntu/ $(lsb_release -sc)
varnish-4.1" | tee -a /etc/apt/sources.list  
  
# update varnish packages  
RUN apt-get update && apt-get clean  
  
# install varnish  
RUN cd /opt && apt-get source varnish && mv /opt/varnish-* /opt/varnish  
WORKDIR /opt/varnish  
RUN ./autogen.sh  
RUN ./configure  
RUN make -j3  
RUN make install  
  
# install varnish libvmod-vsthrottle  
RUN git clone https://github.com/varnish/libvmod-vsthrottle.git /opt/libvmod-
vsthrottle  
WORKDIR /opt/libvmod-vsthrottle  
RUN ./autogen.sh  
RUN ./configure VARNISHSRC=/opt/varnish  
RUN make -j3  
RUN make install  
  
# install varnish libvmod-redis  
RUN git clone https://github.com/carlosabalde/libvmod-redis.git /opt/libvmod-
redis  
WORKDIR /opt/libvmod-redis  
RUN ./autogen.sh  
RUN ./configure VARNISHSRC=/opt/varnish  
RUN make -j3  
RUN make install  
  
ENV LISTEN_ADDR 0.0.0.0  
ENV LISTEN_PORT 8080  
ENV BACKEND_ENV_PORT 5000  
ENV BACKEND_PORT_5000_TCP_ADDR 0.0.0.0  
ENV TELNET_ADDR 0.0.0.0  
ENV TELNET_PORT 6083  
ENV CACHE_SIZE 25MB  
ENV THROTTLE_LIMIT_NUMBER 300  
ENV THROTTLE_LIMIT_TIME 1m  
ENV VCL_FILE /etc/varnish/default.vcl  
ENV GRACE_TTL 30s  
ENV GRACE_MAX 1h  
  
ADD config/default.vcl.source /etc/varnish/default.vcl.source  
ADD bin/run.sh /bin/run.sh  
ADD bin/reload.sh /bin/reload.sh  
RUN chmod +x /bin/reload.sh  
  
EXPOSE 8080  
WORKDIR /  
  
ENTRYPOINT ["/bin/run.sh"]  
CMD []  

