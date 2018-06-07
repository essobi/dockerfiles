FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y \  
curl \  
git \  
psmisc \  
sudo \  
vim \  
zsh  
# docker.io  
# Consider using full docker.io if docker client fails due to compatibility  
# Get the docker client.  
WORKDIR /tmp  
RUN curl -s https://master.dockerproject.org/linux/x86_64/docker.sha256 \  
| sed "s/build\\\/linux\\\/docker\\\/docker/-/g" > docker.sha256 \  
&& curl -s https://master.dockerproject.org/linux/x86_64/docker \  
| tee docker \  
| sha256sum -c docker.sha256 \  
&& mv docker /usr/bin/docker \  
&& chmod ugo+x /usr/bin/docker  
  
# Set up shared volume  
RUN mkdir /var/shared/ \  
&& touch /var/shared/placeholder  
VOLUME /var/shared  
  
WORKDIR /root  
  
# Setup up zsh  
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git .oh-my-zsh  
COPY .glitch_aliases .zshrc .vimrc ./  
  
# Solarized colors  
RUN mkdir -p ~/.vim/autoload ~/.vim/bundle && \  
curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim  
  
WORKDIR /root/.vim/bundle  
RUN git clone git://github.com/altercation/vim-colors-solarized.git  
  
WORKDIR /root  
  
CMD ["/bin/zsh"]  

