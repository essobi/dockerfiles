FROM ubuntu:16.04  
ADD ./* /root/  
  
RUN apt-get update && apt-get install -y \  
git \  
zsh \  
curl \  
vim && \  
chsh -s /bin/zsh root && \  
zsh  
  
RUN zsh /root/init.sh  
  

