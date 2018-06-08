FROM ubuntu:latest  
MAINTAINER Martin Neiiendam mn@lokalebasen.dk  
ENV REFRESHED_AT 2014-02-21  
RUN sed -i.bak 's/main$/main universe/' /etc/apt/sources.list  
  
RUN apt-get update -y  
RUN apt-get install -y python-software-properties build-essential libpq-dev
curl postgresql-client  
RUN apt-add-repository ppa:brightbox/ruby-ng  
  
RUN apt-get update  
RUN apt-get install -y ruby2.0 ruby2.0-dev ruby2.0-doc  
RUN gem install bundler --no-rdoc --no-ri  
RUN gem install etcd -v=0.0.5  
RUN gem install systemu -v=2.6.2  
  
RUN curl -L -o /bin/etcdenv
"https://gist.github.com/fracklen/56cd1440ed3785aadfdf/raw/92d168d931fe5c4132e7bbbd774177cdce0d9ad9/with_etcd_environment"  
RUN chmod +x /bin/etcdenv  
  

