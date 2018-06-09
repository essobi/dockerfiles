FROM alpine:latest  
MAINTAINER AshDev <ashdevfr@gmail.com>  
  
RUN apk upgrade --update && \  
apk add --update util-linux bash tar curl wget vim git zsh tmux nodejs  
  
# USER  
ENV WORK_DIR /root  
WORKDIR $WORK_DIR  
  
# Zsh config  
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh && \  
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc  
  
# Git Aliases  
RUN git config --global alias.co checkout  
RUN git config --global alias.ci commit  
RUN git config --global alias.cp cherry-pick  
RUN git config --global alias.st status  
RUN git config --global alias.br branch  
RUN git config --global alias.r rebase  
RUN git config --global alias.ri rebase -i  
RUN git config --global alias.l '!git --no-pager log --graph
--pretty=format:"%Cred%h%Creset -%C(auto)%d%Creset %s %Cgreen(%cr) %C(bold
blue)<%an>%Creset" --abbrev-commit --date=relative'  
RUN git config --global alias.lg 'log --graph --pretty=format:"%Cred%h%Creset
-%C(auto)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset" --abbrev-commit
--date=relative'  
  
VOLUME $WORK_DIR  
  
ENTRYPOINT ["/bin/zsh"]  

