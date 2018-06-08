FROM centos:latest  
  
MAINTAINER matheuspeschke@hotmail.com  
  
# START OF DEPENDENCIES INSTALL  
RUN yum install -y epel-release  
  
RUN yum install -y wget python-pip python python-devel python34 python34-devel
MySQL-python mysql-devel  
  
# For mysql pip package build  
RUN yum groupinstall -y "Development tools"  
  
# END OF DEPENDENCIES INSTALL  
COPY *.sh /opt/movies/  
COPY burntdvds/auth_api/ /opt/movies/burntdvds/auth_api/  
COPY burntdvds/burntdvds/ /opt/movies/burntdvds/burntdvds/  
COPY burntdvds/movies/ /opt/movies/burntdvds/movies/  
COPY burntdvds/static/ /opt/movies/burntdvds/static/  
COPY burntdvds/templates/ /opt/movies/burntdvds/templates/  
COPY burntdvds/README.rst /opt/movies/burntdvds/  
COPY burntdvds/*.py /opt/movies/burntdvds/  
  
RUN cd /opt/movies/ && bash "04-Install VirtualEnv PipPackages-Production.sh"  
  
ARG MOVIES_ALLOWEDHOSTS_HOSTNAME=localhost  
ARG MOVIES_ALLOWEDHOSTS_IP=127.0.0.1  
ARG MOVIES_DB_NAME=burntdvds  
ARG MOVIES_DB_USER=burntdvds  
ARG MOVIES_DB_PASSWORD=BuRnTdVdS8902348.ovusoiud  
ARG MOVIES_DB_SERVER=127.0.0.1  
ARG MOVIES_DB_PORT=3306  
ARG MOVIES_RUNSERVER_HOST=127.0.0.1  
ARG MOVIES_RUNSERVER_PORT=8000  
ENV MOVIES_ALLOWEDHOSTS_HOSTNAME=${MOVIES_ALLOWEDHOSTS_HOSTNAME} \  
MOVIES_ALLOWEDHOSTS_IP=${MOVIES_ALLOWEDHOSTS_IP} \  
MOVIES_DB_NAME=${MOVIES_DB_NAME} \  
MOVIES_DB_USER=${MOVIES_DB_USER} \  
MOVIES_DB_PASSWORD=${MOVIES_DB_PASSWORD} \  
MOVIES_DB_SERVER=${MOVIES_DB_SERVER} \  
MOVIES_DB_PORT=${MOVIES_DB_PORT} \  
MOVIES_RUNSERVER_HOST=${MOVIES_RUNSERVER_HOST} \  
MOVIES_RUNSERVER_PORT=${MOVIES_RUNSERVER_PORT}  
  
RUN export MOVIES_ALLOWEDHOSTS_HOSTNAME=${MOVIES_ALLOWEDHOSTS_HOSTNAME} && \  
export MOVIES_ALLOWEDHOSTS_IP=${MOVIES_ALLOWEDHOSTS_IP} && \  
export MOVIES_DB_NAME=${MOVIES_DB_NAME} && \  
export MOVIES_DB_USER=${MOVIES_DB_USER} && \  
export MOVIES_DB_PASSWORD=${MOVIES_DB_PASSWORD} && \  
export MOVIES_DB_SERVER=${MOVIES_DB_SERVER} && \  
export MOVIES_DB_PORT=${MOVIES_DB_PORT} && \  
export MOVIES_RUNSERVER_HOST=${MOVIES_RUNSERVER_HOST} && \  
export MOVIES_RUNSERVER_PORT=${MOVIES_RUNSERVER_PORT} && \  
chmod +x /opt/movies/06-Run\ Server.sh  
  
CMD "/opt/movies/burntdvds/bin/python3" /opt/movies/burntdvds/manage.py
runserver ${MOVIES_RUNSERVER_HOST}:${MOVIES_RUNSERVER_PORT}

