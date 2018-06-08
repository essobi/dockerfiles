FROM alpine:3.7  
MAINTAINER packeteer <packeteer@gmail.com>  
  
RUN apk add --no-cache --update zsh openssh rsync tmux git python2 py2-pip
py2-magic py-boto ansible neovim ncurses groff less mailcap  
RUN pip install --upgrade awscli s3cmd  
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh  
  
ADD ./config/.tmux.conf /root/.tmux.conf  
ADD ./config/.zshrc /root/.zshrc  
ENV SHELL=/bin/zsh  
ENV LC_ALL=en_US.UTF-8  
ENTRYPOINT ["zsh"]  

