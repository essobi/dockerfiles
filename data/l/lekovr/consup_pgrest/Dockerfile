# consup_pgrest  
# Consup postgrest image  
# See https://github.com/LeKovr/consup  
#  
FROM lekovr/consup_nginx  
  
MAINTAINER Alexey Kovrizhkin <lekovr+docker@gmail.com>  
  
ENV DOCKERFILE_VERSION_PGREST 170429  
ENV DEBIAN_FRONTEND noninteractive  
ENV INITRD No  
  
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
  
WORKDIR /home/app  
  
# Services started by dbinit.sh  
ENV DBINIT_START "dbrpc"  
# ------------------------------------------------------------  
# Backend server config  
# postgresql hostname  
ENV PG_HOST db.service.consul  
  
# postgrest database & user  
ENV DB_NAME dbrpc  
  
# postgrest database template  
# if none set used default (template1)  
ENV DB_TEMPLATE ""  
# postgrest user password  
ENV DB_PASS SET_DB_PASS_HERE_OR_IN_fidm.yml  
  
# key to create db via dbcc service  
ENV DBCC_KEY SET_YOUR_DBCC_KEY_HERE_OR_IN_fidm.yml  
  
# Port dbcc listen on  
ENV DBCC_PORT 5480  
# Secret used to encrypt and decrypt JWT tokens  
ENV JWT_KEY SET_YOUR_JWT_KEY_HERE_OR_IN_fidm.yml  
  
# postgrest API schema  
ENV DB_SCHEMA public  
  
# dbrpc shemas list  
ENV DBRPC_SCHEMAS dbrpc,public  
  
# dbrpc allowed origins  
ENV DBRPC_ORIGIN *  
  
ENV APPUSER op  

