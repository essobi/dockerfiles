FROM debian:sid  
RUN echo "deb http://ftp.jp.debian.org/debian/ sid main" >
/etc/apt/sources.list  
RUN apt-get update && apt-get install ruby-dev ruby build-essential ruby-dev
ruby build-essential bundler xvfb build-essential libncurses5-dev libreadline-
dev libssl-dev libyaml-dev libmariadbclient-dev libsqlite3-dev libxml2-dev
libxslt-dev libsasl2-dev libsasl2-2 libv8-dev libasound2 libnss3 libgconf-2-4
libxss1 libxtst6 libgtk2.0-0 -y fonts-vlgothic imagemagick && rm -rf
/var/lib/apt/lists/*  
RUN apt-get update && apt-get install -y wget && rm -rf /var/lib/apt/lists/*  
RUN wget https://nodejs.org/dist/v8.6.0/node-v8.6.0-linux-x64.tar.xz && tar
xvf node-v8.6.0-linux-x64.tar.xz && rm node-v8.6.0-linux-x64.tar.xz && cd
node-v8.6.0-linux-x64 && cp -r * /usr/local && cd ../ && rm -rf node* && npm
install -g npm yarn  

