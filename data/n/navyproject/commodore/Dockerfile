FROM ruby:2.1  
RUN gem install thor  
RUN gem install etcd  
  
RUN apt-get update  
RUN apt-get -y install apt-transport-https  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
36A1D7869245C8950F966E92D8576A8BA88D21E9  
RUN sh -c "echo deb https://get.docker.io/ubuntu docker main >
/etc/apt/sources.list.d/docker.list"  
RUN apt-get update  
RUN apt-get -y install lxc-docker-1.0.0  
  
RUN mkdir /var/dev  
WORKDIR /var/dev  
  
ADD Gemfile /var/dev/Gemfile  
ADD Gemfile.lock /var/dev/Gemfile.lock  
  
RUN gem install navyrb  
  
ADD . /var/dev/  
  
RUN bundle install  
  
CMD ["bundle", "exec", "bin/commodore"]  

