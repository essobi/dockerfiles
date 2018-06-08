# GCP Client  
#base image from https://github.com/phusion/baseimage-docker  
FROM phusion/baseimage:0.9.10  
# Maintainer  
MAINTAINER Tobias Meissner "meissner.t@googlemail.com"  
# update system  
RUN apt-get update && apt-get upgrade -y && apt-get dist-upgrade -y  
  
# install some system tools  
RUN apt-get install -y wget python  
  
# install GCP client  
RUN cd /opt && \  
wget -c
https://s3.amazonaws.com/connect.globusonline.org/linux/stable/globusconnectpersonal-
latest.tgz && \  
tar xzf globusconnectpersonal-latest.tgz  
RUN rm /opt/globusconnectpersonal-latest.tgz  
RUN mv /opt/globusconnectpersonal-* /opt/globusconnectpersonal  
  
# Use baseimage-docker's bash.  
# CMD ["/bin/bash"]  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Configure environment  
ENV USER=globus \  
UID=1000 \  
GID=100 \  
HOME=/home/$NB_USER  
  
ADD fix-permissions /usr/local/bin/fix-permissions  
ADD start-globus-connect.sh /opt/globusconnectpersonal/start-globus-connect.sh  
# Create globus user with UID=1000 and in the 'users' group  
# and make sure these dirs are writable by the `users` group.  
RUN useradd -m -s /bin/bash -N -u $UID $USER && \  
fix-permissions $HOME  
  
USER $USER  
VOLUME /globusdata  
  
# Add GCP to PATH  
ENV PATH /opt/globusconnectpersonal/:$PATH  
CMD /opt/globusconnectpersonal/start-globus-connect.sh $SETUP_KEY /globusdata  

