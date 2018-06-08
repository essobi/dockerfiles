# QUIZ expressjs server  
#  
FROM nodesource/wheezy:4.4.5  
RUN apt-get update  
  
RUN apt-get install -y -q --no-install-recommends \  
imagemagick \  
ruby \  
ruby-dev \  
libkrb5-dev \  
mercurial \  
&& apt-get -y autoclean  
RUN gem install compass  
RUN npm install -g npm  
RUN npm install -g pm2  
RUN npm install -g grunt-cli  
RUN npm install -g bower  
  
RUN mkdir /code  
WORKDIR /code  
  
EXPOSE 9000  
EXPOSE 9001  

