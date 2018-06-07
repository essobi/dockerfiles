# consup_powerdns  
# Consup powerdns DNS server image  
# See https://github.com/LeKovr/consup  
#  
FROM lekovr/consup_baseapp  
  
MAINTAINER Alexey Kovrizhkin <lekovr+docker@gmail.com>  
  
ENV DOCKERFILE_VERSION 170429  
#
-------------------------------------------------------------------------------  
# Run custom setup scripts  
ADD setup_*.sh /tmp/  
RUN for f in /tmp/setup_*.sh ; do >&2 echo ">>>> $f" ; . $f ; rm $f ; done  
  
#
-------------------------------------------------------------------------------  
# Setup Consup client  
COPY init.d /init.d  
COPY consul /etc/consul  
COPY supervisor.d /etc/supervisor/conf.d  
COPY skel /skel  
COPY dbsave_pdns.sh /usr/local/bin/  
  
# Services started by dbinit.sh  
ENV DBINIT_START "pdns"  
# ------------------------------------------------------------  
# Backend server config  
# Port DNS listening  
ENV PDNS_PORT 53  
# pdns database host  
ENV DB_HOST common.db.service.consul  
ENV DB_NAME pdns  
ENV DB_PASS SET_DB_PASS_HERE_OR_IN_fidm.yml  
  
# key to create db via dbcc service  
ENV DBCC_KEY SET_DBCC_KEY_HERE_OR_IN_fidm.yml  
  
# Port dbcc listen on  
ENV DBCC_PORT 5480  

