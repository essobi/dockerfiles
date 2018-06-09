FROM ubuntu:precise  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise universe" >>
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install -y python-software-properties python g++ make redis-server
libicu-dev libexpat1  
RUN add-apt-repository ppa:chris-lea/node.js  
RUN apt-get update  
RUN apt-get install -y nodejs  
RUN apt-get install -y git  
RUN apt-get install -y vim  
RUN apt-get install -y naturaldocs  
RUN npm install -g roots  
RUN git config --global user.name "Michiel de Jong"  
RUN git config --global user.email "michiel@unhosted.org"  
RUN git config --global push.default current  
RUN apt-get install -y wget  
RUN apt-get install -y build-essential  
RUN apt-get install -y curl  
RUN apt-get install -y git-core  
RUN apt-get install -y libcurl4-openssl-dev  
RUN apt-get install -y libreadline-dev  
RUN apt-get install -y libssl-dev  
#RUN apt-get install -y libxml2-dev  
#RUN apt-get install -y libxslt1-dev  
RUN apt-get install -y libyaml-dev  
RUN apt-get install -y zlib1g-dev  
RUN wget http://cache.ruby-lang.org/pub/ruby/2.1/ruby-2.1.2.tar.gz  
RUN tar -xzf ruby-2.1.2.tar.gz  
RUN cd ruby-2.1.2 && ./configure  
RUN cd ruby-2.1.2 && make  
RUN cd ruby-2.1.2 && make install  
RUN wget http://production.cf.rubygems.org/rubygems/rubygems-2.3.0.tgz  
RUN tar -xzf rubygems-2.3.0.tgz  
RUN cd rubygems-2.3.0 && ruby setup.rb  
RUN gem install jekyll  
RUN gem update --system  
RUN npm install -g bower  
RUN npm install -g grunt-cli  
RUN npm install -g jshint  
RUN gem install bundler  
RUN ln -s /data/.ssh /root/.ssh  
  
#additions for phantomjs:  
RUN apt-get install -y libfreetype6 libfontconfig  

