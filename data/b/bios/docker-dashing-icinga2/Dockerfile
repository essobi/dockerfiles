FROM centos:centos7  
  
RUN yum makecache  
RUN yum -y install epel-release  
RUN yum -y install git rubygems rubygem-bundler ruby-devel openssl gcc-c++
make nodejs  
  
RUN cd /usr/share && git clone https://github.com/Icinga/dashing-icinga2.git  
WORKDIR /usr/share/dashing-icinga2  
  
RUN gem install bundler  
RUN bundle  
  
EXPOSE 8005  
ENTRYPOINT ["dashing", "start", "-p", "8005"]  

