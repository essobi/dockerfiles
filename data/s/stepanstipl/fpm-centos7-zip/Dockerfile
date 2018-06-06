FROM centos:centos7  
MAINTAINER Stepan Stipl  
# https://github.com/stepanstipl/  
RUN yum groupinstall 'Development Tools' -y  
RUN yum install ruby-devel -y  
RUN yum install zlib-devel -y  
  
RUN yum install wget -y  
  
RUN gem install fpm  
  
RUN mkdir /output  
WORKDIR /output  
  
COPY ./docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  

