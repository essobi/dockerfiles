FROM debian:latest  
  
RUN apt-get update && \  
apt-get -y install vim zsh wget curl git tree rsync openssh-client zip mysql-
client  
  
RUN rm -rf /var/lib/apt/lists/*  
  
RUN wget -qO /root/.zshrc https://git.grml.org/f/grml-etc-core/etc/zsh/zshrc  
  
COPY zshrc.local /root/.zshrc.local  
COPY vimrc /root/.vimrc  
COPY vim /root/.vim  
  
RUN mkdir /data  
  
WORKDIR /data  
  
CMD zsh  

