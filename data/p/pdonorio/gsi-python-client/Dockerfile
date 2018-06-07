  
# docker run --rm -t -v (pwd):/code -v httpapi_sharedcerts:/opt/certificates
--name pyirods --link eudatapi_icat_1:rodserver irodsgsiclient sleep infinity  
  
FROM ubuntu:16.04  
MAINTAINER "Paolo D'Onorio De Meo <p.donoriodemeo@cineca.it>"  
  
RUN apt-get update && \  
apt-get install -y \  
libglobus-gssapi-gsi-dev globus-proxy-utils \  
telnet vim \  
python-gssapi python-prettytable python-pip \  
&& pip install beeprint \  
&& mkdir /code  
  
ADD gsi.conf /etc/gss/mech.d/gsi.conf  
  
#########################  
# USER  
ENV IRODS_USER "irods"  
ENV IRODS_PASS "icatserver"  
ENV IRODS_ADMIN "rodsminer"  
  
RUN useradd -ms /bin/bash $IRODS_USER  
RUN yes $IRODS_PASS | passwd $IRODS_USER  
RUN adduser $IRODS_USER sudo  
  
ENV X509_CERT_BASE /opt/certificates  
RUN mkdir -p $X509_CERT_BASE && chown $IRODS_USER -R $X509_CERT_BASE  
ENV X509_CERT_DIR $X509_CERT_BASE/caauth  
ENV X509_USER_CERT $X509_CERT_BASE/$IRODS_ADMIN/usercert.pem  
ENV X509_USER_KEY $X509_CERT_BASE/$IRODS_ADMIN/userkey.pem  
  
#########################  
USER $IRODS_USER  
WORKDIR /code  
  
# CMD [ 'sleep', 'infinity' ]  

