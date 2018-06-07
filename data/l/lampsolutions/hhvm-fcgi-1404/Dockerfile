FROM ubuntu:14.04  
MAINTAINER Pavel Litvyak <pvlltvk@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu xenial-backports main" >
/etc/apt/sources.list  
RUN echo "deb http://archive.ubuntu.com/ubuntu xenial main" >>
/etc/apt/sources.list  
RUN echo "deb http://archive.ubuntu.com/ubuntu xenial multiverse" >>
/etc/apt/sources.list  
RUN echo "deb http://archive.ubuntu.com/ubuntu xenial universe" >>
/etc/apt/sources.list  
  
ARG HHVM_VERSION=hhvm  
  
# Installing packages  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get -y install software-properties-common wget nullmailer supervisor
vim php7.0-cli php7.0-mysql php7.0-xml php7.0-curl \  
libnuma1 hostname curl php7.0-gd php7.0-mcrypt php7.0-sqlite3  
  
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0x5a16e7281be7a449  
RUN add-apt-repository "deb http://dl.hhvm.com/ubuntu $(lsb_release -sc) main"  
RUN apt-get update  
  
RUN apt-get -y install ${HHVM_VERSION}  
RUN apt-get clean && apt-get autoremove -y  
  
## Extra binaries  
RUN mkdir /opt/extras  
  
# Scripts  
ADD supervisor-config/ /etc/supervisor/conf.d/  
ADD scripts/ /scripts/  
RUN chmod 755 /scripts/*.sh  
  
RUN rm -f /var/spool/nullmailer/trigger \  
&& mkfifo /var/spool/nullmailer/trigger \  
&& chown mail:root /var/spool/nullmailer/trigger \  
&& chmod 0622 /var/spool/nullmailer/trigger  
  
RUN echo "$POSTFIX_IP smtp" > /etc/nullmailer/remotes  
  
# Exposing HHVM-FastCGI port  
EXPOSE 9000  
# Logging  
RUN sed -i '/hhvm.log.file /c \  
hhvm.log.file = /var/log2/hhvm-error.log' /etc/hhvm/server.ini  
  
# Default command  
CMD ["/scripts/start.sh"]

