FROM centos  
MAINTAINER Joseph Jones  
ENV CHEFDK_VERSION 0.4.0-1  
ENV EDITPR /usr/bin/vi  
WORKDIR /opt  
ADD http://opscode-omnibus-
packages.s3.amazonaws.com/el/6/x86_64/chefdk-${CHEFDK_VERSION}.x86_64.rpm
/opt/chefdk-${CHEFDK_VERSION}.x86_64.rpm  
RUN rpm -Uvh chefdk-${CHEFDK_VERSION}.x86_64.rpm && rm
chefdk-${CHEFDK_VERSION}.x86_64.rpm  
RUN echo PATH=/opt/chefdk/embedded/bin:\$PATH > /etc/profile.d/chefdk.sh  
VOLUME [ "/data" ]  
RUN adduser chef-user  
USER chef-user  
WORKDIR /data  
ENTRYPOINT [ "/bin/bash" ]  

