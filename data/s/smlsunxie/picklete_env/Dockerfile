FROM ubuntu:14.04  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -qy build-essential libssl-
dev git man curl  
  
USER root  
ENV HOME /root  
ENV NODE_VER iojs-v1.8  
RUN git clone https://github.com/creationix/nvm.git $HOME/.nvm  
  
RUN echo '. ~/.nvm/nvm.sh' >> $HOME/.profile  
  
RUN /bin/bash -l -c "nvm install ${NODE_VER}; nvm alias default ${NODE_VER};"  
  
RUN /bin/bash -l -c "npm install -g grunt-cli && \  
npm install -g bower && \  
npm install -g mocha"  
  
RUN apt-get install -y openssl libreadline6 libreadline6-dev curl zlib1g
zlib1g-dev libssl-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt-
dev autoconf libc6-dev ncurses-dev automake libtool bison subversion pkg-
config  
  
# install RVM, Ruby, and Bundler  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
RUN \curl -L https://get.rvm.io | bash -s stable  
RUN /bin/bash -l -c "rvm requirements"  
RUN /bin/bash -l -c "rvm install 2.0"  
RUN /bin/bash -l -c "rvm use 2.0 --default"  
  
RUN /bin/bash -l -c "gem install bundler --no-ri --no-rdoc"  
RUN /bin/bash -l -c "gem install compass"  
RUN /bin/bash -l -c "gem install bootstrap-sass"  
  
RUN apt-get install -y python  
RUN apt-get install -y GraphicsMagick  
  
# export NVM_DIR="/home/deploy/.nvm"  
# [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"  

