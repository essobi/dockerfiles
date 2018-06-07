FROM ubuntu:16.04  
RUN apt-get update  
  
# install base tools  
RUN apt-get install -y git nano curl  
  
# install ruby  
RUN apt-get install -y ruby ruby-bundler ruby-compass && \  
echo 'gem: --no-document' > /etc/gemrc  
  
# install nodejs  
RUN curl -sL https://deb.nodesource.com/setup_8.x -o nodesource_setup.sh \  
&& chmod +x nodesource_setup.sh && bash nodesource_setup.sh \  
&& apt-get install -y nodejs build-essential  
  
# install sass  
RUN gem install sass  
RUN gem install --pre sass-css-importer  
  
# install npm tools  
RUN npm install -g grunt-cli  
RUN npm install -g gulp-cli  
RUN npm install -g webpack  
RUN npm install -g nodemon  
RUN npm install -g bower  
  
# install yarn  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update && apt-get install yarn  
  
# clean  
RUN apt-get clean && apt-get autoclean && apt-get autoremove -y  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /var/www

