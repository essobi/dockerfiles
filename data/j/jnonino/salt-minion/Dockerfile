FROM centos:6  
LABEL maintainer="Julian Nonino <noninojulian@outlook.com>"  
  
RUN yum update --assumeyes && \  
yum install --assumeyes epel-release initscripts && \  
yum clean expire-cache && \  
yum install --assumeyes salt-minion  
  
COPY start.sh /usr/local/bin  
ENTRYPOINT [ "/usr/local/bin/start.sh" ]

