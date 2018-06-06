  
##########################################################################  
FROM ubuntu:16.04  
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
wget git expect \  
lsof sudo libfuse2 libjson-perl \  
unixodbc odbc-postgresql postgresql-client super \  
python python-psutil python-requests python-jsonschema \  
libglobus-gssapi-gsi4 libglobus-gss-assist3 \  
&& apt-get clean  
  
##########################################################################  
# IRODS icat server  
# install instructions: https://docs.irods.org/4.1.5/manual/installation  
WORKDIR /tmp  
ENV IRODS4VERSION 1.9  
ENV IRODSVERSION 4.$IRODS4VERSION  
# note: there is no releases for ubuntu 16 at the moment...?  
ENV OSVERSION ubuntu14  
# ENV OSVERSION ubuntu16  
ENV IRODSFTP "ftp://ftp.renci.org/pub/irods"  
ENV IRODSRELEASES "$IRODSFTP/releases/$IRODSVERSION/$OSVERSION"  
RUN wget -q $IRODSRELEASES/irods-icat-${IRODSVERSION}-${OSVERSION}-x86_64.deb  
RUN wget -q $IRODSRELEASES/irods-database-plugin-
postgres-${IRODS4VERSION}-${OSVERSION}-x86_64.deb  
ENV GSIVERSION 1.2  
ENV IRODSGSI "$IRODSFTP/plugins/irods_auth_plugin_gsi/${GSIVERSION}"  
ENV IRODSGSI_DEB /opt/gsi.deb  
RUN wget -q $IRODSGSI/irods-auth-plugin-
gsi-${GSIVERSION}-${OSVERSION}-x86_64.deb -O $IRODSGSI_DEB  
  
  
##########################################################################  
# install scripts  
ADD expect_irods.sh /tmp/expect_irods  
ADD install_irods.sh /install  
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
## How it should be...  
# Saving configuration files for persistence on irods modifications  
#VOLUME /etc/irods  
#################  
## The bad hack: (please change it in future docker releases)  
## I'm forced to install deb files to save the configuration  
## when volumes mapping would probably be available and easy  
RUN yes $IRODS_PASS | sudo -S dpkg -i irods*.deb  
  
#################  
# Remove remote validation  
USER root  
RUN sed -i '36s/https[^\"]\\+/off/' /etc/irods/server_config.json  
USER $IRODS_USER  
  
#################  
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

