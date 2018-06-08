FROM ligo/software:el7  
  
LABEL name="LIGO RPM Test - Staging" \  
maintainer="Adam Mercer <adam.mercer@ligo.org>" \  
date="20170826" \  
support="Reference Platform"  
  
# initialise metadata  
RUN yum makecache  
  
# enable production-staging, testing, and staging repositories  
RUN yum -y install lscsoft-production-staging-config \  
lscsoft-testing-config \  
lscsoct-staging-config  
  
# install any updates and clear cache  
RUN yum clean all && \  
yum makecache && \  
yum -y update && \  
yum clean all  

