FROM centos:centos7  
MAINTAINER Stepan Stipl  
# https://github.com/stepanstipl/  
RUN rpm -Uvh https://yum.puppetlabs.com/puppetlabs-release-pc1-el-7.noarch.rpm  
RUN yum install puppet -y  
RUN yum groupinstall 'Development Tools' -y  
RUN yum install zlib-devel -y  
  
ENV PATH "/opt/puppetlabs/puppet/bin/:$PATH"  
RUN gem install fpm  
  
RUN mkdir /output  
WORKDIR /output  
  
ENV RPM_PREFIX puppetlabs-rubygem  
ENV DEPENDENCIES false  
  
COPY ./docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  

