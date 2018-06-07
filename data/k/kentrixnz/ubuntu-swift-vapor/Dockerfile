FROM ibmcom/swift-ubuntu  
MAINTAINER qianzhi.huang@thewarehouse.co.nz  
  
# Just add Vapor  
RUN /bin/bash -c "$(wget -qO- https://apt.vapor.sh)"  
RUN apt-get install -yq swift vapor clang clang-3.4 postgresql postgresql-
contrib libpq-dev  

