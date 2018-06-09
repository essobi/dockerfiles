FROM ubuntu:12.04  
MAINTAINER cpswan  
  
# add universe repository to /etc/apt/sources.list  
# we need it for rubygems  
RUN sed -i s/main/'main universe'/ /etc/apt/sources.list  
  
# make sure everything is up to date - update and upgrade  
RUN apt-get update && apt-get upgrade -y  
  
# install rubygems, MySQL lib and unzip  
RUN apt-get install -y rubygems libmysqlclient-dev unzip  
  
# install gems  
RUN gem install sinatra sinatra-contrib data_mapper dm-mysql-adapter --no-rdoc
--no-ri  
  
# copy and install sinatra-ToDoMVC application  
ADD https://github.com/cpswan/sinatra-ToDoMVC/archive/docker.zip /opt/sinatra-
ToDoMVC.zip  
RUN cd /opt && unzip /opt/sinatra-ToDoMVC.zip  
  
# default port for Sinatra is 4567  
EXPOSE 4567  
# run the ToDoMVC app  
CMD /usr/bin/ruby /opt/sinatra-ToDoMVC-docker/app.rb  
  
# example usage:  
# sudo docker run -d -p 4567:4567 -name todomvc_app -link todomvc_db:db
cpswan/todomvc.sinatra  

