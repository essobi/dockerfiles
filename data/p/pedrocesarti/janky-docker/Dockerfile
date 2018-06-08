FROM ubuntu:trusty  
  
MAINTAINER Pedro Cesar <pedrocesar.ti@gmail.com>  
  
RUN mkdir -p /app/  
WORKDIR /app/janky  
EXPOSE 9393  
RUN apt-get update  
RUN apt-get install -y git-core curl zlib1g-dev build-essential libssl-dev
libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev
libcurl4-openssl-dev libffi-dev libmysqlclient-dev  
  
RUN apt-get install -y ruby ruby-dev && gem install bundler  
RUN git clone https://github.com/github/janky.git /app/janky  
RUN cd /app/janky/  
  
RUN apt-get install -y mysql-server  
ADD scripts/init_janky.sh /app/janky/  
  
CMD bash -c /app/janky/init_janky.sh  

