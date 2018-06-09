FROM ubuntu:trusty  
MAINTAINER AshDev <ashdevfr@gmail.com>  
  
RUN apt-get update  
  
RUN apt-get install -y curl wget vim git zsh tmux  
  
# USER  
RUN useradd -ms /bin/zsh user  
RUN adduser user sudo  
RUN echo 'user ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers.d/user  
ENV WORK_DIR /home/user  
USER user  
WORKDIR $WORK_DIR  
  
# Zsh config  
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh && \  
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc  
  
# NVM  
ENV NVM_DIR=$WORK_DIR/.nvm  
ENV NODE_VERSION 5.7.1  
RUN NVM_VERSION="$(curl -s -L http://latest.nvm.sh -o /dev/null -D - | grep
-Ei '^Location: .*tag/v[0-9.]+' | grep -oEi 'v[0-9.]+')" && \  
curl -o-
https://raw.githubusercontent.com/creationix/nvm/$NVM_VERSION/install.sh |
bash && \  
echo '[[ -r $NVM_DIR/bash_completion ]] && . $NVM_DIR/bash_completion' >>
~/.zshrc && \  
. $HOME/.nvm/nvm.sh && \  
nvm install $NODE_VERSION && \  
nvm alias default $NODE_VERSION && \  
nvm use default && \  
npm install -g gulp del grunt-cli bower  
  
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

