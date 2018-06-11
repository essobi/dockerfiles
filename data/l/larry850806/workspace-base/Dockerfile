FROM debian:jessie  
  
# setup workspace  
WORKDIR /root/workspace  
COPY ./config ./config  
  
# set time zone  
ENV TZ "Asia/Taipei"  
# update, install zsh, tmux, wget  
RUN apt-get -y update && \  
apt-get -y install zsh tmux vim wget curl git ca-certificates locales make
procps && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean  
  
# install oh-my-zsh, tmux and setup config files  
RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh
-O - | zsh || true && \  
mv config/.tmux.conf ~ && \  
mv config/.zshrc ~ && \  
rm -rf ~/.oh-my-zsh/themes/* && \  
mv config/bira.zsh-theme ~/.oh-my-zsh/themes && \  
mv config/myScript ~ && \  
rmdir config  
  
# set correct locale  
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \  
dpkg-reconfigure --frontend=noninteractive locales && \  
update-locale LANG=en_US.UTF-8  
  
CMD ["zsh"]  

