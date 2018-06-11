FROM centos:centos7  
MAINTAINER pcman312 <pcman312@gmail.com>  
  
WORKDIR /tmp/  
  
# Setup stuff for ansible  
RUN curl -O http://mirror.centos.org/centos/7/extras/x86_64/Packages/epel-
release-7-9.noarch.rpm  
RUN rpm -ivh epel-release-7-9.noarch.rpm  
  
# Install tools & libraries  
RUN yum install wget rsync git ansible \  
zip openssh-clients \  
libtool gcc gcc-c++ make rpm-build \  
ruby ruby-devel \  
npm \  
-y  
RUN gem install fpm  
  
# Install golang  
RUN curl -LOs https://dl.google.com/go/go1.10.2.linux-amd64.tar.gz  
RUN tar -C /usr/local -xzf go1.10.2.linux-amd64.tar.gz  
ENV PATH="/usr/local/go/bin/:${PATH}"  
# Install zeromq  
WORKDIR /opt/  
RUN curl -LOs
https://github.com/zeromq/zeromq4-1/releases/download/v4.1.5/zeromq-4.1.5.tar.gz  
RUN tar -xzf zeromq-4.1.5.tar.gz  
WORKDIR /opt/zeromq-4.1.5  
RUN ./autogen.sh  
RUN ./configure  
RUN make  
#RUN make check  
RUN make install  
RUN echo /usr/local/lib > /etc/ld.so.conf.d/local.conf  
RUN ldconfig  
RUN cp ./src/libzmq.pc /usr/lib64/pkgconfig/  
  
# Install awscli  
WORKDIR /tmp  
RUN curl -O https://bootstrap.pypa.io/get-pip.py  
RUN python2.7 get-pip.py  
RUN pip install awscli  
  
# Install jq  
RUN wget http://stedolan.github.io/jq/download/linux64/jq  
RUN chmod +x ./jq  
RUN mv ./jq /usr/bin  
  
# Set up .ssh folders  
RUN mkdir -p /root/.ssh/sockets  
  
# Set up user(s)  
RUN useradd blackbird  
RUN mkdir -p /home/blackbird  

