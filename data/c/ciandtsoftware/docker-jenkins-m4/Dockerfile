FROM ciandtsoftware/jenkins-aws  
  
MAINTAINER CI&T-TEAM  
  
USER root  
  
RUN apt-get update \  
&& apt-get install -y libcurl4-openssl-dev libxml2-dev libxslt1-dev
libsqlite3-dev libmysqlclient-dev libpq-dev libevent-dev libreadline-dev
build-essential  
  
RUN gem install pkgr compass  
  
RUN mkdir /home/ubuntu && chown jenkins:jenkins /home/ubuntu  
  
RUN apt-get update && apt-get install -y software-properties-common  
  
# Install Java 8.  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get remove -y openjdk-7-jdk && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
USER jenkins  

