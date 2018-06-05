FROM centos:centos6  
  
MAINTAINER Naoki AINOYA <ainonic@gmail.com>  
  
WORKDIR /tmp  
  
RUN rpm -ivh http://ftp-
srv2.kddilabs.jp/Linux/distributions/fedora/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
  
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
  
# Install Ruby  
RUN git clone https://github.com/sstephenson/ruby-build.git /opt/ruby-build  
RUN chmod u+x /opt/ruby-build/install.sh  
RUN /opt/ruby-build/install.sh  
RUN /usr/local/bin/ruby-build 2.1.2 /opt/ruby-2.1.2  
RUN ln -s /opt/ruby-2.1.2/bin/ruby /usr/local/bin/ruby  
  
# Install mod_mruby  
RUN git clone https://github.com/matsumoto-r/mod_mruby.git /tmp/mod_mruby  
WORKDIR /tmp/mod_mruby  
RUN chmod u+x ./build.sh  
RUN ./build.sh  
RUN make install  
  
# Add PATH  
RUN rm /usr/local/bin/ruby  
RUN find /opt/ruby-2.1.2/bin/* | xargs -I {} ln -s {} /usr/local/bin  

