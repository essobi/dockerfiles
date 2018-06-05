#  
# Node.js, Bundler, Bower & Grunt Dockerfile  
#  
#  
# Pull base image.  
FROM dockerfile/nodejs-bower-grunt  
  
#Set locale  
RUN locale-gen de_DE.UTF-8  
ENV LANG de_DE.UTF-8  
ENV LANGUAGE de_DE:en  
ENV LC_ALL de_DE.UTF-8  
#Install Ruby  
RUN apt-get update  
RUN apt-get -y install ruby2.0 libmysqlclient-dev ruby2.0-dev  
  
RUN rm /usr/bin/ruby /usr/bin/gem /usr/bin/irb /usr/bin/rdoc /usr/bin/erb  
RUN ln -s /usr/bin/ruby2.0 /usr/bin/ruby  
RUN ln -s /usr/bin/gem2.0 /usr/bin/gem  
RUN ln -s /usr/bin/irb2.0 /usr/bin/irb  
RUN ln -s /usr/bin/rdoc2.0 /usr/bin/rdoc  
RUN ln -s /usr/bin/erb2.0 /usr/bin/erb  
RUN gem update --system  
RUN gem pristine --all  
  
#Install Bundler  
RUN gem install --no-user-install bundler  
  
# Define working directory.  
WORKDIR /data  
  
# Define default command.  
CMD ["grunt"]  
  

