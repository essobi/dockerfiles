# Dockerfile for a Rails application using Nginx and Unicorn  
# Select ubuntu as the base image  
FROM ubuntu  
  
# Install nginx, nodejs and curl  
RUN apt-get update -q  
RUN apt-get install -qy nginx  
RUN apt-get install -qy curl  
RUN apt-get install -qy nodejs  
RUN apt-get install -qy libtool  
RUN apt-get install -qy libgmp-dev  
RUN apt-get install -qy libmysqlclient-dev  
RUN apt-get install -qy imagemagick  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# Install rvm, ruby, bundler  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
RUN curl -sSL https://get.rvm.io | bash -s stable  
RUN /bin/bash -l -c "rvm requirements"  
RUN /bin/bash -l -c "rvm install 2.2.2"  
RUN /bin/bash -l -c "gem install bundler --no-ri --no-rdoc --version '1.10.0'"  
  
# Add configuration files in repository to filesystem  
ADD ./config/container/nginx-sites.conf /etc/nginx/sites-enabled/default  
ADD ./config/container/start-server.sh /usr/bin/start-server  
RUN chmod +x /usr/bin/start-server  
  
# Add rails project to project directory  
ADD ./ /rails  
  
# set WORKDIR  
WORKDIR /rails  
  
# bundle install  
RUN /bin/bash -l -c "bundle install"  
RUN /bin/bash -l -c "whenever -w"  
# Publish port 80  
EXPOSE 80  
# Startup commands  
ENTRYPOINT /usr/bin/start-server  

