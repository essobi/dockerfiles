FROM debian:jessie  
MAINTAINER Johannes 'fish' Ziemke <fish@freigeist.org> @discordianfish  
  
RUN apt-get -qy update && apt-get -qy install haproxy ucarp openssl
daemontools  
  
ADD . /haproxy  
WORKDIR /haproxy  
ENTRYPOINT [ "./scripts/run" ]  

