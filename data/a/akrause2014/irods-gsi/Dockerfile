##########################################################################  
FROM ubuntu:15.10  
MAINTAINER "Paolo D'Onorio De Meo <p.donoriodemeo@cineca.it>"  
  
##########################################################################  
# Base setup  
ENV DEBIAN_FRONTEND "noninteractive"  
RUN apt-get update && apt-get upgrade -y  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
  
##########################################################################  
# Install dependencies  
RUN apt-get update && apt-get install -y \  
wget git expect nano \  
lsof sudo libfuse2 libjson-perl \  
unixodbc odbc-postgresql postgresql-client super \  
python python-psutil python-requests python-jsonschema \  
&& apt-get clean  
  
##########################################################################  
### Globus GSI dependencies  
WORKDIR /tmp  
RUN wget -q http://toolkit.globus.org/ftppub/gt6/installers/repo/globus-
toolkit-repo_latest_all.deb  
RUN dpkg -i globus-toolkit-repo_latest_all.deb  
RUN apt-get update  
RUN yes | apt-get -f install  
RUN yes | apt-get install globus-gsi  
  
##########################################################################  
# IRODS icat server  
# install instructions: https://docs.irods.org/4.1.5/manual/installation  
WORKDIR /tmp  
ENV IRODSVERSION 4.1.8  
ENV IRODSFTP "ftp://ftp.renci.org/pub/irods/releases/$IRODSVERSION/ubuntu14"  
RUN wget -q $IRODSFTP/irods-icat-${IRODSVERSION}-ubuntu14-x86_64.deb  
RUN wget -q $IRODSFTP/irods-database-plugin-postgres-1.8-ubuntu14-x86_64.deb  
  
##########################################################################  
# install scripts  
ADD expect_irods.sh /tmp/expect_irods  
ADD install_irods.sh /install  
ADD extras.sh /extras  
# boot up script  
ADD bootstrap.sh /bootup  
CMD ["/bootup"]  
  
##########################################################################  
# A default system PostgreSQL installation is configured for ident-based auth  
# means the unix service account name must match the database user name  
ENV IRODS_USER "irods"  
ENV IRODS_PASS "icatserver"  
RUN useradd -ms /bin/bash $IRODS_USER  
RUN yes $IRODS_PASS | passwd $IRODS_USER  
RUN adduser $IRODS_USER sudo  
USER $IRODS_USER  
  
##########################################################################  
# install simple CA  
RUN yes $IRODS_PASS | sudo -S apt-get install globus-simple-ca  
RUN echo -e "$GSI_NEWUSER_NAME" | grid-cert-request -nopw  
RUN yes | sudo grid-ca-sign -in /home/$IRODS_USER/.globus/usercert_request.pem
-out /home/$IRODS_USER/.globus/usercert.pem  
  
  
  
  
##########################################################################  
## How it should be...  
# Saving configuration files for persistence on irods modifications  
#VOLUME /etc/irods  
  
## The bad hack. Change it in future docker releases,  
## when volumes mapping would probably be available and easy  
RUN yes $IRODS_PASS | sudo -S dpkg -i irods*.deb  
# Installed, so enable persistence  
RUN mkdir copy && rsync -av /etc/irods/ copy/etcirods/  
  
##########################################################################  
# Install irods + connect to postgres  
# Then run the following setup script:  
# sudo /var/lib/irods/packaging/setup_irods.sh  
  
# Resource Server ?  
# https://docs.irods.org/4.1.5/manual/installation/#resource-server  
  
##########################################################################  
# Closing operations  
ENV TERM xterm  
WORKDIR /home/$IRODS_USER  
EXPOSE 1247  
ENV IRODS_HOST rodserver  
# if you need to add future commands after irods installation,  
# use the following  
ENV EXTRA_INSTALLATION_SCRIPT /extras

