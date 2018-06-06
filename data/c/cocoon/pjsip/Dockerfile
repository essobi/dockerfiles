# pjsip builder  
FROM debian:wheezy  
MAINTAINER cocoon  
  
# the volume where to store the result packages  
VOLUME /packages  
  
  
# Stop debconf from complaining about missing frontend  
ENV DEBIAN_FRONTEND noninteractive  
  
# setup  
RUN apt-get update && apt-get clean  
  
# install build tools  
RUN apt-get install -y curl build-essential make gcc wget git-core nano  
  
# install python tools  
RUN apt-get install -y openssh-server libxml2-dev python python-dev python-pip
libsqlite3-dev sqlite3 swig  
  
# install pjsip dependencies  
#RUN apt-get install -y alsa-lib openssh  
  
  
# setup pjsip source  
ADD /projects /projects  
WORKDIR /projects  
  
  
  
#  
# pjsua 2.1.1  
#  
#  
git clone git@gitlab.com:orange-soft-iva/pjproject-2.1.git  
  
  
  
#  
# pjsua 2.1.0  
#  
  
# ims configuration  
#ADD /files/pjlib/include/pj/config_site.h
/projects/pjproject-2.1.0/pjlib/include/pj/config_site.h  
  
# install python pjsua command  
#ADD /files/python_pjsip_install.sh /projects/pjproject-2.1.0/  
#RUN chmod +x /projects/pjproject-2.1.0/python_pjsip_install.sh  
  
  
  
#  
# pjsua 2 2.3  
#  
  
#ADD /files/pjlib/include/pj/config_site.h
/projects/pjproject-2.3/pjlib/include/pj/config_site.h  
  
# install python pjsua command  
#ADD /files/python_pjsip_install.sh /projects/pjproject-2.3/  
  
  
  
CMD /bin/bash  
  
  
  
  
  

