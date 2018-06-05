FROM centos  
MAINTAINER Brian (bex) Exelbierd <bex@pobox.com>  
  
# Update the container  
RUN yum -y update && yum clean all  
  
# Install the appropriate software  
RUN yum install -y epel-release && yum clean all  
RUN yum install -y python-pip && yum clean all  
RUN pip install yaml2ical==0.5.0  
  
# Setup working directory  
WORKDIR /workdir  
  
# Labels - today atomic run will not work :(  
LABEL RUN docker run --rm=true \--privileged -u \${SUDO_UID}:\${SUDO_GID} -v
`pwd`:/workdir \${IMAGE}  
  
ENTRYPOINT ["/usr/bin/yaml2ical"]  

