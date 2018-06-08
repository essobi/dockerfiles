FROM ubuntu:14.04  
MAINTAINER Marc Bachmann <marc@livingdocs.io>  
  
RUN apt-get update && apt-get upgrade -y && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes --no-install-
recommends \  
apt-transport-https build-essential ca-certificates lsb-release python-all
rlwrap \  
curl git nano \  
imagemagick postgresql-client \  
  
# required to build .deb files  
devscripts debhelper fakeroot \  
  
# cleanup  
&& apt-get autoremove -y && apt-get clean && \  
rm -Rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV NVM_SYMLINK_CURRENT true  
ENV PATH=$PATH:/usr/share/nvm/current/bin  
RUN git clone https://github.com/creationix/nvm.git /usr/share/nvm && cd
/usr/share/nvm && git checkout `git describe --abbrev=0 --tags`  
RUN echo '. /usr/share/nvm/nvm.sh' >> /root/.bashrc  
  

