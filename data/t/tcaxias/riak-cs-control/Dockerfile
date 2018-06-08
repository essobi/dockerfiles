# Container for Riak CS Control  
FROM centos:7  
MAINTAINER Tiago Caxias http://github.com/tcaxias  
  
ENV \  
PKGS="pygpgme openssl sudo epel-release python-setuptools" \  
EPEL_PKGS="nginx httpd-tools" \  
RIAK_IP="127.0.0.1" \  
RIAK_PORT="8098" \  
S3_HOST="s3.amazonaws.com" \  
RIAK_CS_PORT="80" \  
RIAK_CS_PROTOCOL="http" \  
RIAK_CS_PROXY_HOST="127.0.0.1" \  
RIAK_CS_PROXY_PORT="8080" \  
PASSWD="big_bad_secret" \  
HTPASS="unsafe_secret" \  
CS_CONTROL="http://s3.amazonaws.com/downloads.basho.com/riak-cs-
control/1.0/1.0.2/rhel/6/riak-cs-control-1.0.2-1.el6.x86_64.rpm"  
RUN \  
yum install -y $CS_CONTROL $PKGS && \  
yum install -y $EPEL_PKGS && \  
easy_install pip && \  
pip install -U pip && \  
pip install supervisor && \  
yum clean -y all  
  
ADD \  
start_riak_cs_control.sh \  
start_nginx.sh \  
nginx.conf \  
supervisord.conf \  
/app/  
  
RUN chmod +x /app/*.sh  
  
WORKDIR /app  
EXPOSE 80  
CMD [ "supervisord", "-j", "/dev/shm/supervisor.pid", "-t", "-c",
"/app/supervisord.conf" ]  

