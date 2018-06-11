FROM buildpack-deps:xenial-curl  
MAINTAINER Life Trading <technology@lifetrading.com.au>  
  
RUN locale-gen en_AU.UTF-8  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANG en_AU.UTF-8  
ENV LC_CTYPE en_AU.UTF-8  
ENV LC_ALL en_AU.UTF-8  
ARG USER=developer  
ENV HOME /home/${USER}  
ARG SHELL=bash  
  
# Change default server and install dependencies  
RUN sed -i
"s/http:\/\/archive.ubuntu.com\/ubuntu\//http:\/\/mirror.internode.on.net\/pub\/ubuntu\/ubuntu\//g"
/etc/apt/sources.list && \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y \  
sudo \  
${SHELL} && \  
rm -rf /var/lib/apt/lists/*  
  
ENV SHELL /bin/${SHELL}  
  
# Change the user that we're running as  
RUN useradd -d /home/${USER} -G sudo -s ${SHELL} -U -m ${USER} && \  
echo "%sudo ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers.d/custom  
  
USER ${USER}  
WORKDIR ${HOME}  

