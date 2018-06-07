FROM ergomentum/centos:7.2.160911182133  
MAINTAINER \  
Ergomentum <build@ergomentum.org>  
  
LABEL \  
vendor="Ergomentum" \  
license="Apache 2.0"  
  
ENV \  
OVH_ENDPOINT="ovh-eu"  
VOLUME \  
["/target"]  
  
COPY \  
lego /usr/bin  
  
COPY \  
entrypoint.sh /  
  
ENTRYPOINT \  
["/entrypoint.sh"]  

