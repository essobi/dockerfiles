FROM ubuntu:latest  
  
MAINTAINER Jay Sun <jaysunsky@gmail.com>  
  
ENV DEPENDENCIES git-core build-essential autoconf libtool libssl-dev  
ENV BASEDIR /tmp/shadowsocks-libev  
ENV SS_PORT 443  
ENV SS_SERVER_ADDR 0.0.0.0  
ENV SS_METHOD aes-256-cfb  
ENV SS_PASSWORD password  
ENV VERSION v2.4.1  
# Set up building environment  
RUN apt-get update \  
&& apt-get install -y $DEPENDENCIES  
  
# Get the latest code, build and install  
RUN git clone https://github.com/shadowsocks/shadowsocks-libev.git $BASEDIR  
WORKDIR $BASEDIR  
RUN git checkout $VERSION \  
&& ./configure \  
&& make \  
&& make install  
  
# Tear down building environment and delete git repository  
WORKDIR /  
RUN rm -rf $BASEDIR/shadowsocks-libev\  
&& apt-get --purge autoremove -y $DEPENDENCIES  
  
RUN apt-get install -y openssh-server  
RUN mkdir /root/.ssh  
RUN echo "ssh-rsa
AAAAB3NzaC1yc2EAAAADAQABAAABAQCs18ilArJyS8FBwjiHP9GVcNyaujWs+B2YNdWb6r6Bh64gGsMjcqCSSvnAO5cVhiKHndV13jSGNljrMfHLTrikQ5EMOPuKBRlS4UnCebMBWhNDbEXBK6iDeKoekkvdbVhKeh9twTSTzqEZQwvYp61xC/z28U7vxPAr2A5E4M1Bg083RIV8CdvDYXbhMQEEzPqULiNF1PewTj4Hkdi9lIambCPiyHeFSaw+VBKCr4lLnKuSeO4rfgNEJJr7uqAv8Mjwg68BY+ryUoaF/85AYEDa+DvhGEze/dwc5/zhcm5s8wfr//X57EVAfMuvD0jgZnUrQacceqhRSSRiggTlUVc9"
> /root/.ssh/authorized_keys  
# Port in the json config file won't take affect. Instead we'll use 443.  
EXPOSE $SS_PORT  
EXPOSE 22  
ADD start.sh /start.sh  
RUN chmod 755 /start.sh  
CMD ["sh", "-c", "/start.sh"]  

