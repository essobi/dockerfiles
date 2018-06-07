# ===========================================  
# infotechsoft/htcondor  
# SEE: http://research.cs.wisc.edu/htcondor  
# ===========================================  
FROM infotechsoft/java:8  
ARG HTCONDOR_VERSION=8.6.9  
LABEL name="infotechsoft/htcondor" \  
vendor="INFOTECH Soft, Inc." \  
version="${HTCONDOR_VERSION}" \  
release-date="2017-11-16"  
MAINTAINER Thomas J. Taylor <thomas@infotechsoft.com>  
  
# HTCondor - default port for the condor_collector  
ENV SHARED_PORT 9618  
ARG SUBMIT_USER=submit  
  
RUN yum -y update && \  
yum -y install curl && \  
curl -o /etc/yum.repos.d/condor.repo
http://research.cs.wisc.edu/htcondor/yum/repo.d/htcondor-stable-rhel7.repo &&
\  
rpm --import http://research.cs.wisc.edu/htcondor/yum/RPM-GPG-KEY-HTCondor &&
\  
yum -y install --enablerepo=centosplus condor-${HTCONDOR_VERSION} && \  
yum -y clean all && \  
useradd -m -g condor -u 1000 ${SUBMIT_USER}  
  
# Configure HTCondor  
RUN echo -e "DISCARD_SESSION_KEYRING_ON_STARTUP = False\n\  
TRUST_UID_DOMAIN = True\n\  
ALLOW_WRITE = *\n\  
USE_SHARED_PORT = True\n\  
SHARED_PORT_PORT = ${SHARED_PORT}\n" >> /etc/condor/condor_config.local  
  
# Expose HTCondor shared port  
EXPOSE ${SHARED_PORT}  
# Expose volumes HTCondor logs and configuration  
VOLUME ["/usr/local/condor/logs", "/etc/condor", "/home/${SUBMIT_USER}"]  
WORKDIR /home/${SUBMIT_USER}  
  
# Running condor_master directly from ENTRYPOINT isn't supported by HTCONDOR
(pid=1) fails  
# Use '/bin/true' to allow condor_master to spawn under PID!=1  
ENTRYPOINT /bin/true && /usr/sbin/condor_master -f -t

