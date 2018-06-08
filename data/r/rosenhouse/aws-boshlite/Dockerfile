FROM ubuntu:14.04  
# install dependencies  
RUN apt-get -qq update  
RUN apt-get -qqy install wget git-core curl zlib1g-dev build-essential libssl-
dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev
libxslt1-dev libcurl4-openssl-dev python-software-properties golang git  
  
# install ruby  
RUN wget http://ftp.ruby-lang.org/pub/ruby/2.1/ruby-2.1.2.tar.gz  
RUN tar -xzvf ruby-2.1.2.tar.gz  
RUN cd ruby-2.1.2/ && ./configure && make && make install  
  
# install bosh CLI  
RUN gem install bosh_cli --no-ri --no-rdoc  
  
# install go & set GOPATH  
RUN mkdir -p /opt/go  
ENV GOPATH /opt/go  
ENV PATH $PATH:$GOPATH/bin  
  
# install spiff  
RUN go get github.com/cloudfoundry-incubator/spiff  
  
# install vagrant  
RUN cd /tmp/ && wget
https://dl.bintray.com/mitchellh/vagrant/vagrant_1.7.2_x86_64.deb && dpkg -i
vagrant_1.7.2_x86_64.deb && vagrant plugin install vagrant-aws  
  

