FROM debian:latest  
MAINTAINER cluelessjoe@github  
  
VOLUME /opt/webroot  
EXPOSE 8080  
ENV NODE_VERSION iojs  
ENV HOME /home  
ENV NVM_DIR $HOME/.nvm  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh && \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
# needed for sane user  
adduser \  
# needed by node  
build-essential libssl-dev ca-certificates curl  
  
# create "sane" group  
RUN addgroup --gid=1000 sane && \  
# create "sane" user  
adduser --system --uid=1000 \--home $HOME --shell /bin/bash sane >> /dev/null
2>&1 && \  
# install sudo to use it  
echo "sane ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \  
chown -R sane:sane $HOME && \  
mkdir -p /server && \  
chown -R sane:sane /server && \  
chown -R sane:sane /usr/local && \  
# clean-up packages  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean  
  
USER sane  
  
# install node version manager  
RUN touch $HOME/.bashrc && \  
echo $NODE_VERSION > $HOME/.nvmrc && \  
NVM_VERSION="$(curl -s -L http://latest.nvm.sh -o /dev/null -D - | grep -Ei
'^Location: .*tag/v[0-9.]+' | grep -oEi 'v[0-9.]+')" && \  
curl https://raw.githubusercontent.com/creationix/nvm/$NVM_VERSION/install.sh
| sh && \  
# install node  
source $NVM_DIR/nvm.sh && \  
nvm install $NODE_VERSION >> /dev/null 2>&1 && \  
nvm alias default $NODE_VERSION  
nom install -g mocha  
  
ENTRYPOINT ["/bin/bash"]  

