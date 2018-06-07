FROM quay.io/ukhomeofficedigital/centos-base  
MAINTAINER tim.gent@digital.homeoffice.gov.uk  
  
# Install Ruby  
RUN yum -y install ruby ruby-devel gem rubygems unzip gcc rpm-build wget &&
yum groupinstall "Development Tools" -y  
  
RUN gem install fpm  
COPY run.sh /run.sh  
RUN chmod a+x /run.sh  
COPY rpmbuild /root/rpmbuild  
RUN mkdir /rpmbuild  
  
WORKDIR /root  
  
ENTRYPOINT /run.sh  

