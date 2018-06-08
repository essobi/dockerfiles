FROM centos:centos6  
  
MAINTAINER prevs-io  
  
WORKDIR /tmp  
  
# Set time  
RUN cp /usr/share/zoneinfo/Japan /etc/localtime  
  
# Add EPEL  
RUN yum install -y epel-release  
  
RUN export PATH=$PATH:/usr/local/bin  
  
# Install required packages  
RUN yum install -y bison  
RUN yum install -y gcc-c++  
RUN yum install -y git  
RUN yum install -y glibc-headers  
RUN yum install -y hiredis-devel  
RUN yum install -y httpd  
RUN yum install -y httpd-devel  
RUN yum install -y libyaml-devel  
RUN yum install -y openssl-devel  
RUN yum install -y readline  
RUN yum install -y readline-devel  
RUN yum install -y tar  
RUN yum install -y zlib  
RUN yum install -y zlib-devel  
  
# Packages for pool  
RUN yum install -y docker-io  
RUN yum install -y git  
RUN yum install -y cronie  
# For build-screen  
RUN yum install -y npm  
RUN yum install -y bzip2  
# Install supervisord  
RUN yum install -y python-setuptools  
RUN easy_install supervisor  
  
# Install Ruby  
RUN git clone https://github.com/sstephenson/ruby-build.git /opt/ruby-build  
RUN chmod u+x /opt/ruby-build/install.sh  
RUN /opt/ruby-build/install.sh  
RUN /usr/local/bin/ruby-build 2.1.2 /opt/ruby-2.1.2  
RUN ln -s /opt/ruby-2.1.2/bin/ruby /usr/local/bin/ruby  
  
# Install mod_mruby  
RUN git clone https://github.com/prevs-io/mod_mruby.git /tmp/mod_mruby  
WORKDIR /tmp/mod_mruby  
COPY config/build_config.rb /tmp/mod_mruby/  
RUN chmod u+x ./build.sh  
RUN ./build.sh  
RUN make install  
  
# Add PATH  
RUN rm /usr/local/bin/ruby  
RUN /opt/ruby-2.1.2/bin/gem install --no-document bundler  
RUN find /opt/ruby-2.1.2/bin/* | xargs -I {} ln -s {} /usr/local/bin  

