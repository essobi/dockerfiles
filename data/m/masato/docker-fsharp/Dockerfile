FROM phusion/baseimage:0.9.15  
MAINTAINER Masato Shimizu <ma6ato@gmail.com>  
  
# Set correct environment variables.  
ENV HOME /root  
  
# Regenerate SSH host keys.  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
## Enabling the insecure key permanently  
RUN /usr/sbin/enable_insecure_key  
  
## Japanese Environment  
ENV LANG ja_JP.UTF-8  
RUN locale-gen $LANG && update-locale $LANG && \  
ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y python emacs24-nox emacs24-el git byobu wget curl unzip
tree elinks  
  
## Mono/F#  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF  
RUN echo "deb http://download.mono-project.com/repo/debian wheezy main" >
/etc/apt/sources.list.d/mono-xamarin.list && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y mono-devel fsharp mono-vbnc
nuget  
  
RUN mozroots --machine --import --sync --quiet  
  
## Development Environment  
RUN update-alternatives --set editor /usr/bin/vim.basic  
  
ENV USERNAME docker  
ENV HOME /home/${USERNAME}  
  
# Add Un-Root User  
RUN useradd -m -d ${HOME} -s /bin/bash ${USERNAME} && \  
echo "${USERNAME}:${USERNAME}" | chpasswd && \  
mkdir ${HOME}/.ssh ${HOME}/tmp && \  
chmod 700 ${HOME}/.ssh && \  
cp /root/.ssh/authorized_keys ${HOME}/.ssh && \  
chmod 600 ${HOME}/.ssh/authorized_keys && \  
chown -R ${USERNAME}:${USERNAME} ${HOME}/.ssh && \  
echo "export LANG=ja_JP.UTF-8" >> ${HOME}/.profile && \  
echo "docker ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
ADD dotfiles ${HOME}  
RUN chown -R ${USERNAME}:${USERNAME} ${HOME}  
  
## Cask  
RUN curl -fsSkL https://raw.github.com/cask/cask/master/go | python && \  
echo export PATH='${HOME}/.cask/bin:$PATH' >> ${HOME}/.profile && \  
/bin/bash -c 'source ${HOME}/.profile && cd ${HOME}/.emacs.d && cask install'  
  
USER root  
ENV HOME /root  
WORKDIR /root  
  
CMD ["/sbin/my_init"]  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

