FROM ubuntu:14.04.5  
RUN apt-get update  
RUN apt-get install -y --force-yes software-properties-common apt-transport-
https  
RUN apt-key adv --keyserver keys.gnupg.net --recv-keys 09617FD37CC06B54  
RUN add-apt-repository ppa:brightbox/ruby-ng  
RUN apt-add-repository "deb http://llvm.org/apt/trusty/ llvm-toolchain-
trusty-3.9 main"  
RUN apt-add-repository "deb https://dist.crystal-lang.org/apt crystal main"  
RUN apt-add-repository "deb https://deb.nodesource.com/node_0.10 trusty main"  
RUN apt-get update  
  
RUN apt-get install -y --force-yes curl git make automake libtool pkg-config
cmake  
RUN apt-get install -y --force-yes libssl-dev libxml2-dev libyaml-dev libgmp-
dev  
RUN apt-get install -y --force-yes libevent-dev libpcre3-dev  
RUN apt-get install -y --force-yes libcurl4-openssl-dev libssh2-1-dev  
RUN apt-get install -y --force-yes ruby2.3 nodejs clang-3.9 libclang-3.9-dev
llvm-3.9-dev  
  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

