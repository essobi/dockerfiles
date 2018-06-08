FROM debian:7  
MAINTAINER Martin Diederich <martin.diederich@gmail.com>  
  
# set env vars  
ENV container docker  
ENV LC_ALL C  
ENV DEBIAN_FRONTEND noninteractive  
  
# configure apt sources  
RUN echo "deb http://security.debian.org/ wheezy/updates main contrib non-free
\n\  
deb http://ftp.de.debian.org/debian wheezy main contrib non-free \n\  
deb http://ftp.de.debian.org/debian wheezy-updates main contrib non-free \n\  
deb http://ftp.de.debian.org/debian wheezy-backports main" >
/etc/apt/sources.list  
  
# configure apt behaviour  
RUN echo "APT::Get::Install-Recommends "false"; \n\  
APT::Get::Install-Suggests "false"; \n\  
APT::Get::Assume-Yes "true"; \n\  
APT::Get::force-yes "true";" > /etc/apt/apt.conf.d/00-general  
  
# install  
RUN apt-get update  
RUN apt-get install -y apt-utils  
  
# install typical requirements for testing  
RUN apt-get install -y procps ssl-cert ca-certificates apt-transport-https
python sudo curl net-tools netcat6  
  
# install goss  
RUN curl -L https://github.com/aelsabbahy/goss/releases/download/v0.2.6/goss-
linux-amd64 -o /usr/local/bin/goss  
RUN chmod +rx /usr/local/bin/goss  
  
# install docker-detect-proxy.sh  
RUN curl -L https://raw.githubusercontent.com/mdicloud/docker-
helper/master/docker-detect-proxy.sh -o /usr/local/bin/docker-detect-proxy.sh  
RUN chmod +rx /usr/local/bin/docker-detect-proxy.sh  
  
# cleanup  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# finally run script on startup  
ENTRYPOINT ["/usr/local/bin/docker-detect-proxy.sh"]  
CMD ["/bin/bash"]  

