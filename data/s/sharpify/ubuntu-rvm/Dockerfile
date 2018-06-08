FROM ubuntu:trusty  
MAINTAINER Carlo Schiesaro <@CarloSchiesaro>  
ENV REFRESHED_AT 2016-10-04  
USER root  
  
# Update and add some extra packeges  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install build-essential -y  
RUN apt-get install curl -y  
RUN apt-get install imagemagick -y  
RUN apt-get install libcurl4-openssl-dev -y  
RUN apt-get install nodejs -y  
  
# Setup environment  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# Setup User  
RUN useradd --home /home/ubuntu -M ubuntu -K UID_MIN=10000 -K GID_MIN=10000 -s
/bin/bash  
RUN mkdir /home/ubuntu  
RUN chown ubuntu:ubuntu /home/ubuntu  
RUN adduser ubuntu sudo  
RUN echo 'ubuntu ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
USER ubuntu  
  
ENV RUBY_VERSION 2.2.2  
# Install RVM  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
RUN \curl -sSL https://get.rvm.io | bash -s stable  
RUN /bin/bash -l -c 'source ~/.rvm/scripts/rvm'  
  
# Install Ruby  
RUN /bin/bash -l -c 'rvm requirements'  
RUN /bin/bash -l -c 'rvm install ruby $RUBY_VERSION'  
RUN /bin/bash -l -c 'rvm use $RUBY_VERSION --default'  
  
# Install bundler  
RUN /bin/bash -l -c 'gem install bundler --no-doc --no-ri'  
  
# Install passenger / nginx  
RUN /bin/bash -l -c 'gem install passenger --no-doc --no-ri'  
RUN /bin/bash -l -c 'rvmsudo passenger-install-nginx-module'  
  
# Install rails  
RUN /bin/bash -l -c 'gem install rails -v 4.2.7.1 --no-doc --no-ri'  
  
### DEVELOPMENT ONLY ###  
# Expose port 3000 to the Docker host, so we can access it  
# from the outside.  
EXPOSE 3000  
RUN mkdir -p /home/ubuntu/public_html  
WORKDIR /home/ubuntu/public_html  
  
RUN echo "source ~/.rvm/scripts/rvm" >> ~/.bashrc  
  
# In your local machine run the docker like this  
# docker run -itP -v $(pwd):/home/ubuntu/public_html sharpify/ubuntu-rvm  
# bundle install  
# start development server  
# rails s -b 0.0.0.0  

