FROM centos:centos6  
  
MAINTAINER Thomas Gerbet <thomas.gerbet@enalean.com>  
  
RUN yum upgrade -y && \  
yum install -y epel-release && \  
yum install -y nodejs npm && \  
yum clean all  
  
RUN npm install -g nodemon  
  
ENV NODE_ENV dev  
  
VOLUME /nodeapp  
WORKDIR /nodeapp  
  
COPY run.sh /run.sh  
ENTRYPOINT ["/run.sh"]  

