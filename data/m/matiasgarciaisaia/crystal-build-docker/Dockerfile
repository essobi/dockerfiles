FROM ubuntu:16.04  
MAINTAINER Crystal Team <crystal@manas.tech>  
  
RUN apt-get update && \  
apt-get install -y apt-transport-https curl build-essential pkg-config libssl-
dev libedit-dev libgmp-dev libxml2-dev libyaml-dev libreadline-dev git-core &&
\  
echo "deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial-3.9 main" >
/etc/apt/sources.list.d/llvm-3.9.list && \  
curl http://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - && \  
curl https://dist.crystal-lang.org/apt/setup.sh | bash && \  
apt-get update && \  
apt-get install -y llvm-3.9 crystal  
  
CMD ["/bin/bash"]  

