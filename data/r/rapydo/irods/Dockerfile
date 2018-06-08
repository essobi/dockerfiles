  
###################  
FROM ubuntu:17.04  
MAINTAINER "Paolo D'Onorio De Meo <p.donoriodemeo@cineca.it>"  
##############  
### HOW TO ###  
## CREATE A USER  
# iadmin mkuser paolo rodsuser  
# iadmin moduser paolo password tester  
## CLOCK SYNC ISSUES  
# apt-get install -y tzdata  
# unlink /etc/localtime  
# ln -s /usr/share/zoneinfo/Etc/GMT+6 /etc/localtime  
###################  
# Preparation  
WORKDIR /tmp  
# GSI and Grid FTP dependencies + # update to globus toolkit 6  
RUN apt-get update -qq && apt-get install -y \  
wget git vim expect lsof sudo \  
apt-transport-https \  
libxml2 \  
&& wget
https://downloads.globus.org/toolkit/gt6/stable/installers/repo/deb/globus-
toolkit-repo_latest_all.deb \  
&& dpkg -i *.deb \  
&& apt-get update -qq && apt-get install -y \  
globus-proxy-utils \  
globus-gsi-cert-utils-progs globus-simple-ca \  
&& apt-get clean autoclean && apt-get autoremove -y && \  
rm -rf /var/lib/cache /var/lib/log /tmp/*  
  
###################  
# Add repos, download and install  
ENV URL https://packages.irods.org  
RUN wget -qO - $URL/irods-signing-key.asc | apt-key add - \  
&& echo "deb [arch=amd64] https://packages.irods.org/apt/ trusty main" | tee
/etc/apt/sources.list.d/renci-irods.list  
  
# Make sure the main irods user is the same id into HTTP API server  
ENV IRODS_UNAME irods  
ENV IRODS_UID 990  
RUN useradd \  
-r -M -d /home/$IRODS_UNAME -s /bin/bash -p ! \  
\--uid $IRODS_UID $IRODS_UNAME \  
&& mkdir -p /home/$IRODS_UNAME && chown $IRODS_UID /home/$IRODS_UNAME  
  
###################  
# GSI and certificates  
# ENV IRODS_VERSION 4.2.0  
# ENV GSI_VERSION 2.0.0  
ENV IRODS_VERSION 4.2.1  
ENV GSI_VERSION 2.1.0  
RUN apt-get update && apt-get install -y \  
irods-runtime=$IRODS_VERSION irods-icommands=$IRODS_VERSION \  
irods-server=$IRODS_VERSION \  
irods-database-plugin-postgres=$IRODS_VERSION \  
irods-auth-plugin-gsi=$GSI_VERSION \  
&& apt-get clean autoclean && apt-get autoremove -y && \  
rm -rf /var/lib/cache /var/lib/log /tmp/*  
  
# Note: USER and GROUP may be added automatically by irods install scripts  
# certificates  
ENV CERTDIR /opt/certificates  
ENV GRIDCERTDIR /etc/grid-security  
ENV CADIR $CERTDIR/simple_ca  
RUN mkdir -p $CADIR  
  
# irods, x509 and gsi scripts  
COPY ./expect_irods.sh /usr/local/bin/prepare_answers  
COPY add_irods_x509.sh /usr/local/bin/add-irods-X509  
COPY switch_irods_user.sh /usr/local/bin/switch  
RUN chmod +x /usr/local/bin/*  
  
###################  
# Add bash rc commands  
RUN echo "alias berods='HOME=/home/$IRODS_UNAME su -p irods'" >>
/root/.bash_aliases  
RUN echo "\\\necho\\\necho 'Become irods administrator user with the
command:'\\\necho '$ berods'" >> /root/.bashrc  
RUN echo "if [ \"\$IRODS_SWITCH\" != '1' ]; then echo; echo \"Switch to irods
users with the 'switch' cli command\"; echo; fi" >> /home/$IRODS_UNAME/.bashrc  
  
###################  
# VOLUMES  
VOLUME /etc  
VOLUME /var/lib/irods  
VOLUME /opt/certificates  
  
###################  
# OTHER OPERATIONS  
ENV TERM xterm-256color  
  
###################  
# ENTRYPOINT  
# if you need to add future commands after irods installation:  
# allow custom scripts to be executed at launch time  
RUN mkdir /docker-entrypoint.d/  
ENTRYPOINT ["docker-entrypoint"]  
COPY ./docker-entrypoint.sh /usr/local/bin/docker-entrypoint  
  
###################  
# WORKDIR /tmp  
EXPOSE 1247  
CMD ["irods"]  

