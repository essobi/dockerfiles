FROM debian:testing  
MAINTAINER Ghislain LE MEUR <ghislain.lemeur@gmail.com>  
WORKDIR /root  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get -yq install vim-nox curl git cmake automake gcc g++ python python3-dev
python-dev ncurses-term tmux zsh locales-all  
RUN /bin/bash -c "yes Y | bash <(curl
http://raw.githubusercontent.com/gigi206/vim-gigix/master/install.sh -s -L -o
-)"  
RUN /bin/bash -c "bash <(curl -fsSL
http://raw.githubusercontent.com/robbyrussell/oh-my-
zsh/master/tools/install.sh -s -L -o -)" && \  
curl http://raw.githubusercontent.com/gigi206/tmux-gigix/master/demo.zsh -s -L
-o \- > /root/.oh-my-zsh/custom/default.zsh && \  
git clone --depth 1 http://github.com/zsh-users/zsh-syntax-highlighting.git
/root/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting && \  
git clone --depth 1 http://github.com/zsh-users/zsh-autosuggestions.git
/root/.oh-my-zsh/custom/plugins/zsh-autosuggestions && \  
sed -i 's@\\(\s*git\s*\\)@\1 zsh-syntax-highlighting zsh-autosuggestions@g'
/root/.zshrc && \  
echo
"PROMPT='%{\$fg[green]%}%n%{\$fg[white]%}@%{\$fg[magenta]%}%m%{\$fg[white]%}:%{\$fg[cyan]%}%~%{\$reset_color%}
\${ret_status}\$(git_prompt_info)%{\$reset_color%}'" >> /root/.zshrc && \  
curl http://raw.githubusercontent.com/gigi206/tmux-gigix/master/tmux.conf -s
-L -o \- > /etc/tmux.conf  

