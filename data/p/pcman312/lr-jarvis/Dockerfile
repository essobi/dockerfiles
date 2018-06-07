FROM centos:centos7  
MAINTAINER pcman312 <pcman312@gmail.com>  
  
WORKDIR /tmp/  
  
RUN yum install epel-release -y  
RUN yum install git \  
zip wget bc \  
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
  
# Install Consul  
WORKDIR /opt/  
RUN wget
https://releases.hashicorp.com/consul/0.6.3/consul_0.6.3_linux_amd64.zip  
RUN unzip consul_0.6.3_linux_amd64.zip  
RUN rm consul_0.6.3_linux_amd64.zip  
RUN mkdir /var/consul  
RUN mkdir -p /etc/consul.d/{server,bootstrap}  
RUN mv consul /usr/local/bin  
COPY server_config.json /etc/consul.d/server/config.json  
COPY bootstrap_config.json /etc/consul.d/bootstrap/config.json  
  
# Set up user(s)  
RUN useradd blackbird  
RUN mkdir -p /home/blackbird  
  
WORKDIR /tmp  

