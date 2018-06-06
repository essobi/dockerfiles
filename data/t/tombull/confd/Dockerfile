FROM centos:latest  
  
ENV CONFD_VERSION="0.11.0" \  
CONFD_URL="https://github.com/kelseyhightower/confd/releases/download"  
RUN yum \--setopt=tsflags=nodocs -y update \  
&& yum clean all \  
&& yum \--setopt=tsflags=nodocs -y install wget \  
&& wget --no-check-certificate --retry-connrefused -t 5
${CONFD_URL}/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-amd64 -O
/bin/confd \  
&& chmod +x /bin/confd \  
&& yum clean all  

