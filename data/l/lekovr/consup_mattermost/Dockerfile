# consup_mattermost  
# Consup mattermost image  
# See https://github.com/LeKovr/consup  
#  
FROM lekovr/consup_nginx  
  
MAINTAINER Alexey Kovrizhkin <lekovr+docker@gmail.com>  
  
ENV DOCKERFILE_VERSION_MATTERMOST 170518  
#
-------------------------------------------------------------------------------  
# Run custom setup scripts  
ADD setup_*.sh /tmp/  
RUN for f in /tmp/setup_*.sh ; do >&2 echo ">>>> $f" ; . $f ; rm $f ; done  
  
#
-------------------------------------------------------------------------------  
# SSHD staff  
ENV APPUSER op  
  
COPY init.d /init.d  
  
#
-------------------------------------------------------------------------------  
# Setup Consup client  
COPY consul /etc/consul  
COPY supervisor.d /etc/supervisor/conf.d  
COPY skel /skel  
  
WORKDIR /home/app  
  
# Services started by dbinit.sh  
ENV DBINIT_START "mattermost"  
# ------------------------------------------------------------  
# Backend server config  
# postgresql hostname  
ENV PG_HOST db.service.consul  
  
# postgrest database & user  
ENV DB_NAME mattermost  
  
# postgrest user password  
ENV DB_PASS SET_DB_PASS_HERE_OR_IN_fidm.yml  
  
# key to create db via dbcc service  
ENV DBCC_KEY SET_YOUR_DBCC_KEY_HERE_OR_IN_fidm.yml  
  
# Port dbcc listen on  
ENV DBCC_PORT 5480  
# dir for export/import database  
ENV DB_DUMPDIR /opt/shared/dump  
  
# ------------------------------------------------------------  
# App config  
# config will be under this dir  
VOLUME ["/opt/mattermost/config"]  
  
ENV APP_PORT 3000  

