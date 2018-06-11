FROM ruby:2.3  
#RUN gem install sass && gem install compass  
RUN gem install compass  
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash - && \  
apt-get install -y --force-yes nodejs  
RUN npm install -g bower && npm install --global gulp-cli  
RUN apt-get install -y zip

