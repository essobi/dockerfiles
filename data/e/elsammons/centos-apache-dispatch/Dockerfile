FROM centos:latest  
MAINTAINER Eric L Sammons <elsammons@gmail.com>  
LABEL version="0.01" description="Creates an Apache-Dispatch-Router contaner
running on CentOS Latest."  
  
RUN useradd -U -m dispatch  
RUN yum -y update  
RUN yum groupinstall -y "Development Tools"  
RUN yum install -y python-devel cmake make gcc git swig ruby-devel php-devel
perl-devel cyrus-sasl-devel cyrus-sasl-plain cyrus-sasl-gssapi cyrus-sasl-md5
openssl-devel libuuid-devel epydoc  
  
RUN git clone https://github.com/apache/qpid-proton.git  
RUN cd qpid-proton && mkdir my_build && cd my_build && cmake ..
-DCMAKE_INSTALL_PREFIX=/usr -DSYSINSTALL_BINDINGS=O && make install  
RUN git clone https://github.com/apache/qpid-dispatch.git  
RUN cd qpid-dispatch && mkdir my_build && cd my_build && cmake ..
-DCMAKE_INSTALL_PREFIX=/usr && make && ctest -VV && make install  
  
RUN mv /etc/qpid-dispatch/qdrouterd.conf /home/dispatch/.  
  
##  
# Expose the AMQP port.  
#  
EXPOSE 5672  
##  
# Lets run dispatch as a non-root user  
##  
USER dispatch  
  
CMD qdrouterd -c /home/dispatch/qdrouterd.conf  
  

