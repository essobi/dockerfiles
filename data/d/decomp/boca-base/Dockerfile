# VERSION 0.1  
FROM ubuntu:xenial  
  
RUN apt-get -y update  
RUN apt-get -y install tzdata locales software-properties-common python-
software-properties --no-install-recommends  
RUN echo "America/Sao_Paulo" > /etc/timezone; dpkg-reconfigure -f
noninteractive tzdata  
RUN locale-gen en_US en_US.UTF-8  
RUN locale -a  
ENV LANGUAGE=en_US.UTF-8  
ENV LANG=en_US.UTF-8  
ENV LC_ALL=en_US.UTF-8  
RUN locale-gen en_US.UTF-8  
RUN DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales  
  
RUN add-apt-repository ppa:brunoribas/ppa-maratona  
RUN apt-get -y update  
RUN apt-get -y install maratona-boca --no-install-recommends --allow-
unauthenticated  
RUN apt-get -y clean  

