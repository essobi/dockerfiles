FROM cpuguy83/debian:jessie  
  
RUN apt-get update -qq && apt-get install -y make curl -qq && apt-get clean  
  
ADD https://github.com/postmodern/ruby-install/archive/v0.4.3.tar.gz /tmp/  
RUN cd /tmp && tar -zxvf v0.4.3.tar.gz && cd /tmp/ruby-install-0.4.3 && make
install  

