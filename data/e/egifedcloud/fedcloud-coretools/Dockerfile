# Dockerfile for building a EGI FedCloud userinterface  
FROM ubuntu:xenial  
MAINTAINER Enol Fernandez <enol.fernandez@egi.eu>  
  
ADD fedcloud-ui.sh /tmp/fedcloud-ui.sh  
  
RUN DEBIAN_FRONTEND=noninteractive /tmp/fedcloud-ui.sh  
  
# extra tools for docker image: myproxy  
RUN apt-get -y install myproxy  
# and OpenStack CLI + VOMS  
RUN apt-get -y install python-pip  
RUN pip install openstack-voms-auth-type  
RUN pip install python-swiftclient  
RUN cat /etc/grid-security/certificates/*.pem >> $(python -m requests.certs)  
  
RUN fetch-crl -v || true  
  
WORKDIR /data  
  
# Create occi user, give sudo privileges  
RUN useradd -m occi  
RUN apt-get -y install sudo  
RUN echo "occi ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/80-occi-user  
RUN chmod 0440 /etc/sudoers.d/80-occi-user  
RUN chown -R occi /etc/grid-security/certificates /data  
USER occi  
  
# /etc/grid-security/certificates keeps the CRLs  
# /tmp keeps the proxy files  
VOLUME [ "/etc/grid-security/certificates", "/tmp" ]  

