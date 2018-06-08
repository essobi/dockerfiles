FROM ubuntu:14.04.1  
MAINTAINER Masato Shimizu <ma6ato@gmail.com>  
  
ENV NODE_VERSION v0.10  
ENV USERNAME docker  
ENV HOME /home/${USERNAME}  
  
RUN useradd -m -d ${HOME} -s /bin/bash ${USERNAME} && \  
echo "${USERNAME}:${USERNAME}" | chpasswd && \  
echo "${USERNAME} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y curl git build-essential  
  
ENV USERNAME docker  
ENV HOME /home/${USERNAME}  
  
USER ${USERNAME}  
WORKDIR ${HOME}  
  
RUN git clone git://github.com/creationix/nvm.git ${HOME}/.nvm && \  
/bin/bash -c 'source ${HOME}/.nvm/nvm.sh && \  
nvm install ${NODE_VERSION} && \  
nvm use ${NODE_VERSION} && \  
nvm alias default ${NODE_VERSION}' && \  
echo '[[ -s "${HOME}/.nvm/nvm.sh" ]] && source "${HOME}/.nvm/nvm.sh"' >>
${HOME}/.profile && \  
/bin/bash -c 'source ${HOME}/.profile && \  
npm install -g npm && \  
npm config set python /usr/bin/python2.7 && \  
npm install -g strongloop && \  
npm cache clear'  
  
EXPOSE 3000 53322  
USER root  
ENV HOME /root  
WORKDIR /root  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

