FROM python:2.7  
MAINTAINER Person Sebastien <personseb@yahoo.fr>  
  
# no need for confirmation  
ENV DEBIAN_FRONTEND noninteractive  
  
# see http://www.garron.me/en/blog/ubuntu-deb-proxy-cache.html  
#RUN echo 'Acquire::http { Proxy "http://192.168.0.32:3142"; };' >
/etc/apt/apt.conf.d/use-local-proxy  
RUN apt-get -qq update  
  
# Recommends are as of now still abused in many packages  
RUN echo 'APT::Install-Recommends "0";' >> /etc/apt/apt.conf.d/no-recommends  
RUN echo "APT::Get::Assume-Yes "true";" > /etc/apt/apt.conf.d/always-yes  
  
RUN apt-get -y install git-core  
WORKDIR /domoweb  
RUN git clone git://github.com/domogik/domoweb.git /domoweb  
RUN git submodule update --init --recursive  
  
# update sources  
RUN git pull  
  
RUN apt-get -q -y install adduser  
  
RUN adduser --system domoweb --shell /bin/sh  
  
## first run : init all the part except db  
RUN ln -sf /usr/local/bin/python /usr/bin/  
#RUN ./install.py -u domoweb --nodbupdate --notest  
#RUN ./install.py -u domoweb --nodeps --notest --noconfig  
#CMD /etc/init.d/domoweb start && tail -f /var/log/domoweb/console.log  
EXPOSE 40404  
#  
# manque : pyzmq  
#libzmq-dev  
# debug  
RUN apt-get install net-tools libzmq-dev nano

