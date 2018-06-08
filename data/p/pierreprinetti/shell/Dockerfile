FROM alpine:3.7  
RUN apk add --no-cache build-base ncurses tmux bash zsh curl git go python3
perl vim ctags  
  
ENV HOME=/root  
ENV DOTFILES=${HOME}/.dotfiles  
  
# Install custom dotfiles  
COPY . ${DOTFILES}  
RUN ${DOTFILES}/install/symlinks.sh -f  
RUN ${DOTFILES}/install/zsh-plugins.sh  
RUN ${DOTFILES}/install/vim-plugins.sh  
RUN ${DOTFILES}/install/tmux-plugins.sh  
  
RUN zsh zplug update  
  
ENTRYPOINT ["zsh"]  

