FROM ruby:slim  
  
RUN \  
unlink /etc/localtime ;\  
ln -s /usr/share/zoneinfo/Japan /etc/localtime ;\  
sed -i -e 's@http://archive@http://jp.archive@' /etc/apt/sources.list  
RUN apt-get update -qq  
RUN apt-get install -y -qq \  
git locales build-essential libicu-dev cmake pkg-config libsqlite3-dev ruby-
execjs  
RUN locale-gen ja_JP.UTF-8  
  
RUN (cd /srv && git clone https://github.com/asm-products/octobox.git)  
WORKDIR /srv/octobox  
RUN apt-get install -y -qq \  
npm mongodb-server redis-server  
RUN npm install -g bower  
RUN npm install -g grunt-cli  
RUN gem install sass  
RUN apt-get install -y -qq \  
nodejs-legacy  
RUN npm update -g npm  
RUN npm update -g bower  
RUN npm update -g grunt-cli  
RUN npm install  
RUN sed -i -e '/angular-ui-codemirror/d' bower.json  
RUN bower install --allow-root  
EXPOSE 3000  
CMD service mongodb start && service redis-server start && grunt  

