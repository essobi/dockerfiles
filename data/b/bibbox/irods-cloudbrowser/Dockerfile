# iRODS Cloud Browser  
#  
# VERSION 0.0.2  
#  
# 0.0.1 : initial creation of image for iRODS Cloud Browser  
# 0.0.2 : splitting up the iRODS Cloud Browser frontend and backend  
FROM httpd:2.4  
MAINTAINER Robert Reihs <robert.reihs@gmail.com>  
  
RUN apt-get update \  
&& apt-get -y upgrade \  
&& apt-get -y install unzip wget \  
&& wget https://github.com/DICE-UNC/irods-cloud-
browser/releases/download/1.0.1-RELEASE/irods-cloud-frontend.zip  
  
RUN rm /usr/local/apache2/htdocs/index.html \  
&& unzip irods-cloud-frontend.zip \  
&& rm irods-cloud-frontend.zip \  
&& mv irods-cloud-frontend/* /usr/local/apache2/htdocs/ \  
&& rm -r irods-cloud-frontend  
  
ADD scripts /opt/scripts  
WORKDIR /opt/scripts  
RUN chmod a+x *.sh  
  
ENTRYPOINT ["/opt/scripts/entrypoint.sh"]

