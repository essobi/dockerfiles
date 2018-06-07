FROM theswolf/base-no-ui  
  
USER root  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
# Install base dependencies  
RUN apt-get update && apt-get install -y -q --no-install-recommends \  
apt-transport-https \  
build-essential \  
ca-certificates \  
curl \  
git \  
libssl-dev \  
python \  
rsync \  
software-properties-common \  
wget \  
bash \  
&& rm -rf /var/lib/apt/lists/*  
  
#enable bash  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
USER developer  
ENV
NVM_URL=https://raw.githubusercontent.com/creationix/nvm/v0.33.0/install.sh  
ENV NODE_VERSION=6.9.4  
# Install nvm with node and npm  
RUN echo '' > .bashrc  
RUN curl $NVM_URL | bash \  
&& source /home/developer/.bashrc \  
&& nvm install $NODE_VERSION \  
&& nvm alias default $NODE_VERSION \  
&& nvm use default  

