FROM ruby:2.2.1  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections && \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee
/etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 &&
\  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
apt-get install -y oracle-java8-set-default  
ENV DOCKER true  
WORKDIR /tmp  
ADD ./Gemfile Gemfile  
ADD ./Gemfile.lock Gemfile.lock  
RUN bundle install  
ADD . /opt/apoapsis  
WORKDIR /opt/apoapsis  
RUN mkdir data  
ENTRYPOINT ./startup.sh  
EXPOSE 3000  

