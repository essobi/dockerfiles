FROM debian:jessie  
  
#Install curl, supervisor, openssh-server, git  
RUN apt-get update && apt-get install -y curl openssh-server supervisor git  
RUN mkdir -p /var/run/sshd /var/log/supervisor  
  
#Install node js  
RUN curl -sL https://deb.nodesource.com/setup | bash -  
RUN apt-get install -y nodejs  
  
#install ruby  
RUN apt-get install -y ruby-full  
  
#install sass  
RUN gem install sass  
  
#install mongo  
RUN apt-get update  
RUN apt-get install -y mongodb  
  
#Install angular fullstack generator  
RUN npm install -g generator-angular-fullstack  
  
#Install bower  
RUN npm install -g bower  
  
#Install grunt  
RUN npm install -g grunt-cli  
  
#Install yeoman  
RUN npm install -g yo  
  
#Install gulp  
RUN npm install -g gulp  
  
#install graphics magick  
RUN apt-get install -y graphicsmagick  

