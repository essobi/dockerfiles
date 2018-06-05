FROM ubuntu:latest  
# install build dependencies (and vim ;-) )  
RUN apt update  
# todo: we probably don't need all of this. vim is just for debugging  
RUN apt install -y wget curl tzdata vim net-tools software-properties-common  
  
# add the tor key  
RUN gpg --keyserver keys.gnupg.net --recv
A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89  
RUN gpg --export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 | apt-key add -  
  
# add the globaleaks key  
RUN wget -qO - https://deb.globaleaks.org/globaleaks.asc | apt-key add -  
RUN add-apt-repository universe  
RUN add-apt-repository 'deb http://deb.torproject.org/torproject.org xenial
main'  
RUN add-apt-repository 'deb http://deb.globaleaks.org xenial/'  
  
# install globaleaks  
RUN apt update  
RUN apt install -y globaleaks  
  
RUN sed -i -n -e '/^APPARMOR_SANDBOXING=/!p' -e '$aAPPARMOR_SANDBOXING=0'
/etc/default/globaleaks  
RUN sed -i -n -e '/^NETWORK_SANDBOXING=/!p' -e '$aNETWORK_SANDBOXING=0'
/etc/default/globaleaks  
  
# ports needed for globaleaks  
EXPOSE 80  
EXPOSE 443  
# ports for tor  
EXPOSE 8082  
EXPOSE 8083  
# todo: a better docker entrypoint. Tor needs to run alongside globaleaks. We
could move tor into it's own container, but that makes this image harder to
use.  
COPY ./docker-entrypoint.sh /opt/docker-entrypoint.sh  
RUN chmod +x /opt/docker-entrypoint.sh  
ENTRYPOINT /opt/docker-entrypoint.sh  
VOLUME /var/globaleaks/  
VOLUME /etc/default/  
# todo: this image doesn't shut down gracefully, probably because of the
docker-entrypoint above.  

