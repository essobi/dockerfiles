FROM centos:centos7  
  
ENV KUISP_VERSION 0.10  
RUN yum install -y tar && \  
yum clean all && \  
curl -L
https://github.com/jimmidyson/kuisp/releases/download/v${KUISP_VERSION}/kuisp-${KUISP_VERSION}-linux-
amd64.tar.gz | \  
tar xzv  
  
ENTRYPOINT ["/kuisp"]  
  

