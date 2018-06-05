# docker build -t my/zeronet .  
# docker run -d --name zeronet -v ~/.zeronetdata:/data -p 43110:43110
my/zeronet  
FROM alpine:3.7  
MAINTAINER Andrey Arapov <andrey.arapov@nixaid.com>  
  
RUN apk update \  
&& apk add py-gevent py-msgpack ca-certificates python  
  
# Optionally you may want to enable Tor in order to anonymize the traffic  
RUN apk add tor  
RUN echo -e "ControlPort 9051\nSocksListenAddress 0.0.0.0" > /etc/tor/torrc  
# RUN echo -e "ControlPort 9051" > /etc/tor/torrc  
# RUN echo -e "ControlPort 9051\nCookieAuthentication 1" > /etc/tor/torrc  
# RUN adduser $USER tor  
ENV USER=zeronet \  
UID=1000 \  
HOME=/home/zeronet \  
PROJECT_VER=v0.6.2 \  
PROJECT=ZeroNet-0.6.2 \  
DATA=/data  
  
RUN adduser -D -u $UID -h $HOME -s /bin/true $USER  
  
USER $USER  
VOLUME ["$DATA"]  
WORKDIR $HOME  
RUN wget -O data.tar.gz -q
https://github.com/HelloZeroNet/ZeroNet/archive/${PROJECT_VER}.tar.gz \  
&& tar xpzf data.tar.gz \  
&& rm -f data.tar.gz \  
&& cd $PROJECT \  
&& mkdir log \  
&& touch log/error.log \  
&& ln -sv $DATA ./data  
  
# the launch script needs to chown the /data in case when $UID does not match  
# the UID of the host  
USER root  
COPY launch ./$PROJECT/  
CMD ./$PROJECT/launch  

