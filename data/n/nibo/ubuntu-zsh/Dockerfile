FROM nibo/ubuntu:16.04-hk  
MAINTAINER Richard<nibocn@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y git \  
&& apt-get install -y zsh \  
&& git clone --depth 1 https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-
zsh \  
&& cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc \  
&& echo "bindkey '^R' history-incremental-pattern-search-backward" >> ~/.zshrc
\  
&& chsh -s /bin/zsh \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
CMD ["zsh"]  

