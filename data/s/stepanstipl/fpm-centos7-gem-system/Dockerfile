FROM centos:centos7  
MAINTAINER Stepan Stipl  
# https://github.com/stepanstipl/  
RUN yum groupinstall 'Development Tools' -y  
RUN yum install ruby-devel -y  
RUN yum install zlib-devel -y  
  
RUN gem install fpm  
  
RUN mkdir /output  
WORKDIR /output  
  
ENV RPM_PREFIX rubygem  
ENV DEPENDENCIES false  
  
COPY ./docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  

