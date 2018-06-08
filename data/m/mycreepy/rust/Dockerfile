FROM centos:7  
MAINTAINER Tobias Germer  
  
ENV RUST_HOME=/source \  
RUST_VERSION=1.11.0 \  
USER=nobody  
  
WORKDIR $RUST_HOME  
  
RUN yum install wget gcc -y && yum clean all  
RUN wget https://static.rust-lang.org/dist/rust-$RUST_VERSION-x86_64-unknown-
linux-gnu.tar.gz && \  
tar xfz rust-$RUST_VERSION-x86_64-unknown-linux-gnu.tar.gz && \  
$RUST_HOME/rust-$RUST_VERSION-x86_64-unknown-linux-gnu/install.sh && \  
rm -rf $RUST_HOME/* && \  
chown $USER:$USER $RUST_HOME  
  
VOLUME $RUST_HOME  
  
USER $USER  
CMD /bin/bash  

