FROM centos:6  
MAINTAINER billie@purplebooth.co.uk  
  
RUN yum -y install unzip tar gcc-c++ ruby-devel gcc pcre-devel pcre openssl-
devel ruby ruby-devel gem rubygems wget perl rpm-build rpm  
  
RUN gem install fpm  
COPY run.sh /run.sh  
RUN chmod a+x /run.sh  
COPY . /root  
  
WORKDIR /root  
  
ENTRYPOINT /run.sh  
  

