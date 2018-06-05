FROM brownman/nvm  
  
ENV INSTALL_RUBY_VERSION 2.1.0  
ENV CONFIGURE_OPTS --disable-install-doc  
  
  
# install ruby, bundler  
RUN wget -qO - https://raw.github.com/fesplugas/rbenv-
installer/master/bin/rbenv-installer | bash  
ENV RBENV_ROOT ${HOME}/.rbenv  
ENV PATH ${RBENV_ROOT}/bin:${PATH}  
  
RUN rbenv install $INSTALL_RUBY_VERSION  
RUN rbenv global $INSTALL_RUBY_VERSION  
RUN rbenv rehash  
RUN echo "eval \"\$(rbenv init -)\"" >> $HOME/.profile  
RUN echo "eval \"\$(rbenv init -)\"" >> $HOME/.bashrc  
RUN echo 'gem: --no-rdoc --no-ri' >> /$HOME/.gemrc  
RUN . $HOME/.profile && gem install bundler  

