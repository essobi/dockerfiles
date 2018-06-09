FROM debian:jessie-backports  
LABEL maintainer="tyler@heucke.io"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get upgrade -y && apt-get install -y \  
curl \  
git \  
less \  
rsync \  
silversearcher-ag \  
sudo \  
unzip \  
vim \  
wget \  
&& apt-get -t jessie-backports install -y gosu \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /mnt  
VOLUME [ "/mnt" ]  
  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
ENTRYPOINT [ "/usr/local/bin/entrypoint.sh" ]  
CMD [ "bash" ]  
  

