FROM fedora:22  
MAINTAINER Joshua Preston <jpreston@redhat.com>  
  
LABEL Name=atomicmirror  
LABEL Description="a container that is used to host a mirror of atomic rpm-
ostree repositories"  
LABEL Version=1.0  
LABEL Vendor="Red Hat" License=GPLv3  
  
# Setup our locations  
ENV CONFDIR /etc/atomicmirror  
ENV DATADIR /var/lib/atomicmirror  
ENV LOGDIR /var/log/atomicmirror  
  
# Setup the repos we are going to enable for syncing  
ENV OSTREE_ENABLE_REPOS fedora-atomic-22  
# Setup our atomic labels properly  
LABEL INSTALL="docker run --rm --privileged -v /:/host -e HOST=/host -e
LOGDIR=${LOGDIR} -e CONFDIR=${CONFDIR} -e DATADIR=${DATADIR} -e NAME=NAME -e
IMAGE=IMAGE IMAGE /usr/local/bin/install.sh"  
LABEL RUN="docker run -d -v ${CONFDIR} -v ${DATADIR} -v ${LOGDIR} -p 8000 -e
NAME=NAME --name NAME"  
LABEL UNINSTALL="docker run --rm --privileged -v /:/host -e HOST=/host -e
LOGDIR=${LOGDIR} -e CONFDIR=${CONFDIR} -e DATADIR=${DATADIR} \--name NAME -e
NAME=NAME -e IMAGE=IMAGE IMAGE /usr/local/bin/uninstall.sh"  
  
# install needed packages  
RUN dnf upgrade -y; \  
dnf install -y rpm-ostree polipo; \  
dnf clean all  
  
# create required directories  
RUN mkdir -p ${CONFDIR} ${DATADIR} ${LOGDIR}  
  
# install our scripts that does our magical dirty work  
COPY install.sh /usr/local/bin/install.sh  
COPY run.sh /usr/local/bin/run.sh  
COPY uninstall.sh /usr/local/bin/uninstall.sh  
  
RUN chmod +x /usr/local/bin/*.sh  
  
# install our atomicmirror service for systemd  
COPY atomicmirror_template.service
/etc/systemd/system/atomicmirror_template.service  
  
# install our repository configs  
COPY repos ${CONFDIR}/repos  
  
# make sure the volume is exported for retention purposes  
VOLUME ${CONFDIR}  
VOLUME ${DATADIR}  
VOLUME ${LOGDIR}  
  
# expose default SimpleHTTPServer port and set working dir  
EXPOSE 8000  
# make sure we're working out of the data directory  
WORKDIR ${DATADIR}  
  
# Exec our command to host our repository  
CMD [ "/usr/local/bin/run.sh" ]  

