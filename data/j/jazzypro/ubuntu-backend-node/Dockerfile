FROM jazzypro/ubuntu-basic:latest  
  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
  
#  
# Add repositories and update packages list  
#  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get update  
  
#  
# Install node.js and update NPM  
#  
# Fix bug https://github.com/npm/npm/issues/9863  
RUN apt-get install -y nodejs  
RUN node -v  
RUN echo node version $(node -v) >> /root/soft_versions  
RUN cd $(npm root -g)/npm \  
&& npm install fs-extra \  
&& sed -i -e s/graceful-fs/fs-extra/ -e s/fs\\.rename/fs.move/
./lib/utils/rename.js  
RUN npm install npm@latest -g  
RUN npm -v  
RUN echo npm version $(node -v) >> /root/soft_versions  
  
#  
# Setup npm cache proxy  
#  
RUN npm config set proxy http://jazzy.pro:4011/  
RUN npm config set https-proxy http://jazzy.pro:4011/  
RUN npm config set strict-ssl false  
  
#  
# Install SASS/Compass  
#  
RUN apt-get install -y ruby ruby-dev  
RUN gem install sass compass  
RUN ruby -v  
RUN echo $(ruby -v) >> /root/soft_versions  
  
#  
# Install Gulp, Bower, LESS, Webpack  
#  
RUN npm install -g gulp  
RUN npm install -g bower  
RUN npm install -g less  
RUN npm install -g webpack  
  
#  
# Install Composer  
#  
RUN wget -O /bin/composer https://getcomposer.org/composer.phar && chmod a+x
/bin/composer  

