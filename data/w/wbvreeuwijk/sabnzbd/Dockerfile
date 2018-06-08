#SABNzbd  
#  
# Version 0.2  
FROM wbvreeuwijk/nzb-base:latest  
MAINTAINER Bas van Reeuwijk <bas@reeuwijk.net>  
  
LABEL Description="This image will install a SABNzbd server" Version="1.0"  
  
ENV YENC 0.4.0  
RUN apk update \  
&& apk add p7zip  
  
# Install Cheetah  
RUN pip install Cheetah sabyenc  
  
# Create and go to build directory  
RUN mkdir -p /usr/src && cd /usr/src  
  
# Creat par2cmd  
RUN git clone https://github.com/Parchive/par2cmdline.git par2cmdline \  
&& cd par2cmdline \  
&& aclocal \  
&& automake --add-missing \  
&& autoconf \  
&& ./configure \  
&& make \  
&& make check \  
&& make install \  
&& rm -rf par2cmdline  
  
# Create YENC  
RUN wget -O- https://bitbucket.org/dual75/yenc/get/$YENC.tar.gz | tar -zx \  
&& cd dual75-yenc-* \  
&& python setup.py install \  
&& cd .. \  
&& rm -rf dual75-yenc-*  
  
# Get SABNZBD from GitHub and install as sabnzbd user  
USER $SABNZBD_UID  
  
RUN cd /opt && git clone -b master https://github.com/sabnzbd/sabnzbd sabnzbd  
  
# Exposing sabnzbd web ui  
EXPOSE 8080  
USER 0  
# Mount points for volumes  
RUN mkdir -p /downloads/complete \  
&& mkdir -p /downloads/incomplete \  
&& chown -R $SABNZBD_UID /downloads  
  
# Define environement variables  
ENV HOME /config  
  
# Define container volume  
VOLUME ["/config","/downloads/complete","/downloads/incomplete"]  
  
# Setting start CMD  
CMD ["/usr/bin/python", "/opt/sabnzbd/SABnzbd.py", "-f",
"/config/sabnzbd.ini", "-s", "0.0.0.0:8080"]  

