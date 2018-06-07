FROM inspirehep/invenio-base:latest  
MAINTAINER Federico Poli "federico.poli@cern.ch"  
  
#################  
# Configuration #  
#################  
  
RUN /usr/sbin/make-ssl-cert /usr/share/ssl-cert/ssleay.cnf
/etc/apache2/ssl/apache.pem  
  
#####################  
# Create Drone user #  
#####################  
  
RUN useradd --create-home --password drone drone  
RUN chown drone:drone /home/drone  
RUN echo "drone ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
ENV HOME /home/drone  
WORKDIR /home/drone  
USER drone  
  
##############################  
# Prepares files and folders #  
##############################  
  
RUN mkdir ~/.ssh  
ADD invenio-local.conf /home/drone/invenio-local.conf  

