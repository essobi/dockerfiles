FROM ubuntu:artful  
  
RUN apt-get update && \  
apt-get install -y \  
zsh \  
git \  
curl \  
wget \  
screen \  
build-essential && \  
rm -rf /var/lib/apt/lists/* && \  
git clone https://github.com/robbyrussell/oh-my-zsh.git /etc/oh-my-zsh  
  
COPY zshrc /root/.zshrc  
  
SHELL ["/bin/zsh", "-c"]  
  
WORKDIR "/root"  
  
VOLUME ["/root/.history"]  
  
ENV HISTFILE="/root/.history/zsh_history"  
CMD ["/bin/zsh"]  
  

