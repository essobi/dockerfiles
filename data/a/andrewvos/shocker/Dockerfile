FROM stackbrew/ubuntu:raring  
  
#golang  
RUN apt-get install -y --force-yes curl && \  
curl -O https://go.googlecode.com/files/go1.1.2.linux-amd64.tar.gz && \  
tar -C /usr/local -xzf go1.1.2.linux-amd64.tar.gz  
ENV GOPATH /gopath  
ENV PATH $PATH:$GOPATH/bin:/usr/local/go/bin  
  
#ruby 2.0.0  
RUN apt-get install -y --force-yes software-properties-common  
RUN apt-add-repository -y ppa:brightbox/ruby-ng-experimental  
RUN apt-get update  
RUN apt-get install -y --force-yes ruby2.0 ruby2.0-dev build-essential  
RUN gem install bundler --no-rdoc --no-ri --pre  
  
#install git  
RUN apt-get install -y --force-yes git-core  
  
#elasticsearch  
RUN apt-get update && \  
apt-get install -y --force-yes openjdk-7-jre-headless && \  
curl -O
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-0.90.3.deb
&& \  
dpkg -i elasticsearch-0.90.3.deb  
  
#firefox  
RUN apt-get -y --force-yes install firefox xvfb  
ENV DISPLAY :0  
#postgres  
RUN locale-gen en_US.UTF-8  
RUN update-locale LANG=en_US.UTF-8  
RUN apt-get install wget && \  
echo 'deb http://apt.postgresql.org/pub/repos/apt/ squeeze-pgdg main' >>
/etc/apt/sources.list.d/pgdg.list && \  
wget --quiet -O - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | apt-
key add - && \  
apt-get -y update && \  
apt-get -y install postgresql postgresql-contrib libpq-dev  
  
#redis  
RUN apt-get -y install redis-server  

