#  
# PostgreSQL / PostGIS  
#  
# Tutorial for GIS engineers who want to use spatial database in their
projects  
#  
# Set base image  
#  
# It's required to set base image first.  
# All other services will be installed above this image.  
# Base image is set after `FROM` directive as {image_name}:{image_tag}.  
# Image tag is equal to Ubuntu version in the current scope.  
  
FROM ubuntu:16.04  
# Set up image information  
#  
# Current section provides metadata for image.  
# It's used in search results.  
# `\\` symbol is used to split string into several lines  
# e.g LABEL label_name = "label_value" is equal to  
# LABEL \  
# label_name = \  
# label_value  
# White space will be ignored.  
  
LABEL \  
version="1.0.0" \  
maintainer="Sergey Gorodilov (sgorodil@gmail.com)" \  
description="A PostgreSQL/PostGIS training image for GIS engineers." \  
used_software="postgresql,postgis,openssh" \  
openssh_ver="7.2" \  
postgresql_ver="10.3" \  
postgis_ver="2.4" \  
ssh_reference="https://docs.docker.com/engine/examples/running_ssh_service/" \  
postgres_reference="https://docs.docker.com/engine/examples/postgresql_service/"  
# Perform software installation and setting up  
#  
# `RUN` directive is used to run shell commands.  
# First image should sync packages list. After this it's possible to install a
package.  
#  
# `&&` is used to combine several commands.  
# A command after `&&` will be started if the previous command has been
successfully finished.  
# e.g. `touch foobar && echo "foo" > foobar` the echo command will be started
only after  
# successful touch command.  
  
RUN apt-get update \  
&& apt-get install -y apt-utils nano sudo wget python-software-properties
software-properties-common \  
&& echo "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main" >
/etc/apt/sources.list.d/pgdg.list \  
&& wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-
key add - \  
&& apt-get update && apt-get install -y postgresql-10 postgresql-client-10
postgresql-10-postgis-2.4 postgis \  
&& sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'/"
/etc/postgresql/10/main/postgresql.conf \  
&& sed -i "s/127\\.0\\.0\\.1\/32/0\\.0\\.0\\.0\/0 /"
/etc/postgresql/10/main/pg_hba.conf \  
&& apt-get install -y openssh-server \  
&& mkdir /var/run/sshd \  
&& echo 'root:rootpassword' | chpasswd \  
&& sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config \  
&& sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
# Exposing ssh and postgres ports  
EXPOSE 22 5432  
# Run rest as `postgres` user  
USER postgres  
RUN /etc/init.d/postgresql start \  
&& psql -c "ALTER USER postgres WITH PASSWORD 'postgres';"  
# Go back to root  
USER root  
  
# By default the SSH server will started on the container instance start-up  
CMD ["/usr/sbin/sshd", "-D"]  
  
# GIS Forum  
# Kharkov, Ukraine  
# 2018  

