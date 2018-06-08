FROM osixia/openldap:1.1.6  
MAINTAINER mps299792458@gmail.com  
  
ENV FUSIONDIRECTORY_VERSION=1.0.17-1  
  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys E184859262B4981F
\  
&& echo "deb http://repos.fusiondirectory.org/debian-jessie jessie main" \  
> /etc/apt/sources.list.d/fusiondirectory-jessie.list \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
fusiondirectory-schema=${FUSIONDIRECTORY_VERSION} \  
fusiondirectory-plugin-argonaut-schema=${FUSIONDIRECTORY_VERSION} \  
fusiondirectory-plugin-autofs-schema=${FUSIONDIRECTORY_VERSION} \  
fusiondirectory-plugin-gpg-schema=${FUSIONDIRECTORY_VERSION} \  
fusiondirectory-plugin-mail-schema=${FUSIONDIRECTORY_VERSION} \  
fusiondirectory-plugin-postfix-schema=${FUSIONDIRECTORY_VERSION} \  
fusiondirectory-plugin-ssh-schema=${FUSIONDIRECTORY_VERSION} \  
fusiondirectory-plugin-sudo-schema=${FUSIONDIRECTORY_VERSION} \  
fusiondirectory-plugin-systems-schema=${FUSIONDIRECTORY_VERSION} \  
fusiondirectory-plugin-weblink-schema=${FUSIONDIRECTORY_VERSION} \  
fusiondirectory-plugin-webservice-schema=${FUSIONDIRECTORY_VERSION} \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY init.sh /sbin/init.sh  
RUN chmod 755 /sbin/init.sh  
RUN sed -i "/# stop OpenLDAP/i /sbin/init.sh"
/container/service/slapd/startup.sh  

