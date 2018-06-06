FROM ubuntu:saucy  
MAINTAINER Kevin Littlejohn <kevin@littlejohn.id.au>  
  
# Fix the locale  
RUN localedef -c -i en_AU -f UTF-8 en_AU.UTF-8  
  
RUN apt-get -yq update && apt-get -yq upgrade  
  
# Requirements for RoR  
RUN apt-get -yq install ruby2.0-dev  
RUN apt-get -yq install build-essential  
RUN apt-get -yq install ruby2.0  
RUN apt-get -yq install libsqlite3-dev  
RUN apt-get -yq install nodejs  
RUN apt-get -yq install git  
RUN update-alternatives --set ruby /usr/bin/ruby2.0  
# Verbose to stop things from timing out - revisit if we can fix the timeout  
RUN gem2.0 install rails --no-rdoc --no-ri -V  
  
# Add a continuously user  
RUN adduser --disabled-password --gecos "" continuously; \  
echo "continuously ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
VOLUME /var/git  
RUN chown -R continuously.continuously /var/git  
ENV HOME /home/continuously  
  
# Cache buster  
ADD continuously/Gemfile /tmp/Gemfile  
ADD continuously/Gemfile.lock /tmp/Gemfile.lock  
RUN cd /tmp && grep -v docker_peer Gemfile > Gemfile.tmp && mv Gemfile
Gemfile.full && mv Gemfile.tmp Gemfile && bundle install  
ADD continuously/lib/docker_peer /tmp/lib/docker_peer  
RUN cd /tmp && mv Gemfile.full Gemfile && bundle install  
  
# Add the project to the container  
ADD continuously opt/continuously  
RUN chown -R continuously.continuously /opt/continuously  
USER continuously  
WORKDIR /opt/continuously  
  
EXPOSE 3000  
  
CMD ["rails", "s"]  

