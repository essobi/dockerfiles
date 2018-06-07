#  
# Eclipse+PyDev on CentOS 6  
#  
# Markus Juenemann, 25-Nov-2015  
FROM mjuenema/eclipse  
MAINTAINER Markus Juenemann <markus@juenemann.net>  
USER root  
  
# Fetch and install Eclipse/PyDev certificate  
#  
RUN wget --debug -O pydev_certificate.cer
http://www.pydev.org/pydev_certificate.cer  
  
# Install python-pexpect as it is needed for importing the  
# Eclipse/PyDev certificate.  
#  
RUN yum -y install expect  
  
# Add and run the expect file  
#  
RUN keytool -import -file pydev_certificate.cer -keystore
/etc/pki/java/cacerts -storepass changeit -trustcacerts -noprompt  
  
# Install PyDev  
#  
RUN /opt/eclipse/eclipse -nosplash \  
-application org.eclipse.equinox.p2.director \  
-destination /opt/eclipse \  
-repository http://download.eclipse.org/technology/dltk/updates/,http://pydev.org/updates/ \  
-installIU org.python.pydev.feature.feature.group  
  
USER developer  
ENV HOME /home/developer  
WORKDIR /home/developer  
CMD /usr/local/bin/eclipse  

