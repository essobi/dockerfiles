FROM ubuntu:16.04  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN locale-gen en_US.UTF-8  
  
RUN apt-get update && apt-get install -y \  
curl \  
git \  
zsh \  
&& git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh \  
&& chsh -s /bin/zsh  
  
COPY rootfs/ /  
WORKDIR /root  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["zsh"]  

