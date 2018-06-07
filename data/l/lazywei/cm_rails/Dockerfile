FROM lazywei/cm_base:latest  
MAINTAINER Bert Chang "https://github.com/lazywei"  
RUN apt-get install -y nodejs npm  
RUN apt-get install -y memcached  
RUN apt-get install -y ruby-dev libqtwebkit-dev  
  
RUN rbenv install 2.1.2 &&\  
rbenv global 2.1.2  
  
ENV GEM_HOME /ruby_gems/2.1  
VOLUME ["/root/src/codementor"]  
  
ENTRYPOINT memcached -u root -d && bash  

