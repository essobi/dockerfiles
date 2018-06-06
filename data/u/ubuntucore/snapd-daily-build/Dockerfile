FROM ubuntu:xenial  
  
RUN apt update && \  
apt install --no-install-recommends -y -qq \  
ca-certificates \  
devscripts \  
dpkg-dev \  
dput \  
git \  
golang-go \  
libdistro-info-perl \  
lintian \  
sudo && \  
rm -rf /var/lib/apt  
  
RUN adduser --system travis && echo 'travis ALL=(ALL) NOPASSWD: ALL' >>
/etc/sudoers  
  
ENV GOPATH=/go  
ENV SNAPCORE_PATH=${GOPATH}/src/github.com/snapcore  
ENV SNAPD_PATH=${SNAPCORE_PATH}/snapd  
  
RUN mkdir -p $SNAPCORE_PATH && chown -R travis $GOPATH  
  
COPY ./entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

