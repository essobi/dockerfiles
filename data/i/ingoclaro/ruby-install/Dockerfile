# ruby-install  
# ruby-install binary, so we can compile whatever ruby version we want  
# build with: docker build -t ruby-install ruby-install/  
# use: docker run -i ingoclaro/ruby-install ruby 2.0.0-p353 -- --disable-
install-doc  
FROM tianon/centos  
MAINTAINER Ingo Claro, miclaro@gmail.com  
  
RUN yum -y update  
  
# install dependencies  
RUN yum -y install tar bzip2 automake gcc gdbm-devel libffi-devel ncurses-
devel openssl-devel readline-devel zlib-devel  
  
# install ruby-install  
RUN cd /usr/local/src && curl -L https://github.com/postmodern/ruby-
install/archive/v0.3.4.tar.gz | tar xz  
RUN cd /usr/local/src/ruby-install-0.3.4 && make install  
  
ENTRYPOINT ["/usr/local/bin/ruby-install"]  
VOLUME ["/opt/rubies"]

