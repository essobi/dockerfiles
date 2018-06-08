FROM trenpixster/elixir  
  
RUN apt-key adv --fetch-keys http://dl.yarnpkg.com/debian/pubkey.gpg  
  
RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" | tee
/etc/apt/sources.list.d/pgdg.list  
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |
apt-key add -  
  
RUN apt-get update  
  
RUN apt-get install postgresql-9.5 postgresql-contrib-9.5 -y  
  
ENV NVM_DIR /usr/local/nvm  
ENV NODE_VERSION 7.1.0  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.32.1/install.sh | bash  
  
RUN [ -s "$NVM_DIR/nvm.sh" ] \  
&& . "$NVM_DIR/nvm.sh" \  
&& nvm install stable \  
&& nvm alias default stable \  
&& nvm use default  
  
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules  
ENV PATH $NVM_DIR/v$NODE_VERSION/bin:$PATH  
  
RUN apt-get install yarn -y  
  
ENTRYPOINT ["/bin/sh", "-c"]  
  
CMD ["/bin/bash"]  

