FROM amazonlinux  
MAINTAINER Dmitry Kolomiets <kolomiets@gmail.com>  
  
RUN yum install -y gcc; yum clean all  
RUN curl --silent --location https://rpm.nodesource.com/setup_6.x | bash  
RUN yum install -y nodejs gcc-c++  
RUN npm install -g node-gyp  
RUN npm install -g mocha  

