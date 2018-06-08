FROM ubuntu  
MAINTAINER Kaijun Chen <Kaijun.cn@gmail.com>  
  
RUN apt-get update -qqy  
RUN apt-get install -qqy \  
sudo \  
git \  
zsh \  
curl \  
tmux  
# oh-my-zsh  
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-
zsh/master/tools/install.sh)" || true  
RUN sed -i -E "s/^plugins=\\((.*)\\)$/plugins=(\1 tmux)/" ~/.zshrc  
RUN echo "DISABLE_UPDATE_PROMPT=true" >> ~/.zshrc  
RUN chsh -s /bin/zsh  
  
# TMUX  
RUN echo 'set -g mouse on' >> ~/.tmux.conf  
# Cleanup  
RUN apt-get clean -q  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME ["/root/mnt"]  
WORKDIR /root/mnt  
CMD tmux

