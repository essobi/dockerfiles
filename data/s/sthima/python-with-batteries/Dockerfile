FROM python:3.5.1  
MAINTAINER Matheus Marchini <matheus@sthima.com.br>  
  
RUN apt-get update -qq  
RUN apt-get install ruby2.1 -y  
RUN apt-get install ruby`ruby -e 'puts RUBY_VERSION[/\d+\\.\d+/]'`-dev -y  
RUN apt-get install rsync -y  
  
RUN gem2.1 install sass  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install nodejs -y  
  
RUN npm install -g bower less coffeescript yarn  
RUN echo '{ "allow_root": true }' > /root/.bowerrc  

