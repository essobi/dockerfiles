FROM ubuntu:xenial  
MAINTAINER Alex Oberhauser, alex@cambridge-blockchain.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927  
  
RUN echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2
multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list  
RUN apt-get update  
RUN apt-get install -y mongodb-org  
  
RUN apt-get install -qq -y python-software-properties curl  
RUN curl -sL https://deb.nodesource.com/setup_6.x | /bin/bash -  
RUN apt-get install -qq -y nodejs  
RUN apt-get install -qq -y libgdbm-dev libncurses5-dev automake libtool bison
libffi-dev  
RUN apt-get install -qq -y git  
  
RUN curl -sSL https://get.rvm.io | bash -s stable  
RUN /bin/bash -l -c "rvm requirements"  
RUN /bin/bash -l -c "rvm install 2.3.1"  
RUN /bin/bash -l -c "gem install bundler --no-ri --no-rdoc"  
  
COPY entrypoint.sh /sbin/entrypoint.sh  
ENTRYPOINT ["/sbin/entrypoint.sh"]  
  

