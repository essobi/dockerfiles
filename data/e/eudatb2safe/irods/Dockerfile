##########################################################################  
FROM ubuntu:16.04  
MAINTAINER "Paolo D'Onorio De Meo <p.donoriodemeo@cineca.it>"  
  
##########################################################################  
# Base setup and Install dependencies  
ENV DEBIAN_FRONTEND "noninteractive"  
  
# Use apt to install base applications  
RUN apt-get update -qq && \  
apt-get install -y \  
# base utils  
wget git expect lsof sudo nano vim \  
# CLEAN \  
&& apt-get clean autoclean && apt-get autoremove -y && \  
rm -rf /var/lib/cache /var/lib/log  
  
# Add all of the irods/globus/gsi dependencies  
ENV GLOBUSFTP http://toolkit.globus.org/ftppub/gt6/installers  
ENV GLOBUSGSIDEB $GLOBUSFTP/repo/globus-toolkit-repo_latest_all.deb  
RUN echo "install libs" && \  
wget -q $GLOBUSGSIDEB && dpkg -i globus-*repo*.deb && \  
apt-get update -qq && \  
apt-get install -y \  
# base libs  
libfuse2 libjson-perl \  
# db  
unixodbc odbc-postgresql postgresql-client super \  
# python  
python python-psutil python-requests python-jsonschema \  
# gsi irods plugin dependencies  
libglobus-gssapi-gsi4 libglobus-gss-assist3 \  
# globus and proxy  
globus-proxy-utils globus-gsi-cert-utils-progs globus-simple-ca \  
# globus-gsi globus-gridftp \  
# CLEAN \  
&& apt-get clean autoclean && apt-get autoremove -y && \  
rm -rf /var/lib/cache /var/lib/log  
# /var/lib/apt /var/lib/dpkg  
  
##########################################################################  
# IRODS icat server  
# install instructions: https://docs.irods.org/4.1.10/manual/installation  
WORKDIR /tmp  
ENV IRODS4VERSION 1.10  
ENV IRODSVERSION 4.$IRODS4VERSION  
ENV OSVERSION ubuntu14  
# note: there is no releases for ubuntu 16 at the moment...  
# ENV OSVERSION ubuntu16  
  
ENV IRODSFTP "ftp://ftp.renci.org/pub/irods"  
ENV IRODSRELEASES "$IRODSFTP/releases/$IRODSVERSION/$OSVERSION"  
  
RUN wget -q $IRODSRELEASES/irods-icat-${IRODSVERSION}-${OSVERSION}-x86_64.deb  
RUN wget -q $IRODSRELEASES/irods-database-plugin-
postgres-${IRODS4VERSION}-${OSVERSION}-x86_64.deb  
ENV GSIVERSION 1.4  
ENV IRODSGSI "$IRODSFTP/plugins/irods_auth_plugin_gsi/${GSIVERSION}"  
ENV IRODSGSI_DEB /tmp/gsi.deb  
RUN wget -q $IRODSGSI/irods-auth-plugin-
gsi-${GSIVERSION}-${OSVERSION}-x86_64.deb -O $IRODSGSI_DEB  
  
##########################################################################  
# install scripts: to be executed only the first time  
ADD expect_irods.sh /tmp/expect_irods  
ADD install_irods.sh /init  
# normal boot up script  
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
  
# guest for testing certificates  
ENV GSI_USER guest  
RUN useradd -ms /bin/bash $GSI_USER  
# rodsminer for administration with GSI auth  
ENV GSI_ADMIN rodsminer  
RUN useradd -ms /bin/bash $GSI_ADMIN  
  
##########################################################################  
  
# Install irods packages  
RUN dpkg -i irods*.deb  
  
# Saving configurations files/passw/environments for persistence on irods
modifications  
VOLUME /etc  
# VOLUME /etc/irods  
# VOLUME /etc/grid-security  
  
# Remove irods remote validation  
RUN sed -i '36s/https[^\"]\\+/off/' /etc/irods/server_config.json  
  
##########################################################################  
# THE INIT PHASE IS NECESSARY OUTSIDE OF THE DOCKERFILE  
#  
# How to:  
# Install irods + connect to postgres.  
# Then run the following setup script:  
# $ sudo /var/lib/irods/packaging/setup_irods.sh  
  
##########################################################################  
## Closing operations  
  
# add environment for guest  
WORKDIR /home/$GSI_USER  
ADD guest.irods.env.json .irods/irods_environment.json  
RUN chown -R $GSI_USER:$GSI_USER /home/$GSI_USER/.irods  
  
# passwd handling  
ADD handlepassw.sh /pass  
  
# irods user setup  
ENV IRODS_HOST rodserver  
ADD certificates_init.sh /init_certificates  
EXPOSE 1247  
  
# Various  
ENV TERM xterm  
# if you need to add future commands after irods installation,  
# use the following  
ENV EXTRA_INSTALLATION_SCRIPT /extras  
# volumes  
VOLUME /home/$IRODS_USER  
VOLUME /var/lib/$IRODS_USER  
  
# Become irods main user  
USER $IRODS_USER  
WORKDIR /home/$IRODS_USER  
  
ADD new_authority.sh /addusercert  

