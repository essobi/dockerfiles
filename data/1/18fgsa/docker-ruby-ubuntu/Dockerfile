FROM ubuntu:trusty  
  
RUN locale-gen en_US en_US.UTF-8 \  
&& dpkg-reconfigure locales  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# Install general dependencies  
RUN apt-get update && apt-get install -y build-essential git curl libssl-dev
libreadline-dev zlib1g-dev python3-dev  
  
# install nvm and install versions 4 and 6  
ENV NVM_DIR /usr/local/nvm  
ENV NODE_DEFAULT_VERSION 4  
RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.31.3/install.sh |
bash \  
&& . "$NVM_DIR/nvm.sh" \  
&& nvm install $NODE_DEFAULT_VERSION \  
&& nvm install 6 \  
&& nvm use $NODE_DEFAULT_VERSION \  
&& echo 'export OLD_PREFIX=$PREFIX && unset PREFIX' > $HOME/.profile \  
&& echo '[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"' >> $HOME/.profile \  
&& echo 'export PREFIX=$OLD_PREFIX && unset OLD_PREFIX' >> $HOME/.profile  
  
# Install ruby via rvm  
ENV RUBY_VERSION 2.3.1  
RUN \curl -sSL https://get.rvm.io | bash -s stable  
RUN /bin/bash -l -c 'rvm install $RUBY_VERSION && rvm use --default
$RUBY_VERSION'  
RUN echo rvm_silence_path_mismatch_check_flag=1 >> /etc/rvmrc  

