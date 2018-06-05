FROM baseruntime/baseruntime:latest  
  
MAINTAINER Rado Pitonak <rpitonak@redhat.com>  
  
COPY repos/* /etc/yum.repos.d/  
  
RUN sed -i 's|/jkaluza/|/ralph/|g' /etc/yum.repos.d/build.repo && \  
microdnf --nodocs --enablerepo nodejs install nodejs && \  
microdnf clean all  

