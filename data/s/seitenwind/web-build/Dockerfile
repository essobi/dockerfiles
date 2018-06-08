FROM ubuntu  
  
# update package lists  
RUN apt-get update  
  
# install composer  
RUN apt-get -y install git curl php7.0-cli php7.0-curl php7.0-mbstring  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# install sftp  
RUN apt-get -y install openssh-client rsync  
  
# install latest nodejs  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -  
RUN apt-get -y install nodejs  
  
# install ruby  
RUN apt-get -y install gcc make ruby-dev ruby  
RUN apt-get -y -qq install ruby-dev  
RUN echo "gem: --no-rdoc --no-ri" > ~/.gemrc  
RUN gem update --system  
  
# install style compilation tools  
RUN gem install sass  
RUN gem install compass  
  
# install gulp  
RUN npm i -g gulp-cli  
RUN npm i -g gulp  
  
# install angular cli  
RUN npm i -g @angular/cli  

