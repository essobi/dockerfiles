########################################################################  
# Sirius via HTML5 #  
########################################################################  
  
FROM fedora:25  
  
MAINTAINER Neil Mackenzie <neil@mackenziemail.co.uk>  
  
LABEL vendor="RegCommunity"  
LABEL version="0.1"  
LABEL description="Sirius IDE"  
  
ENV HOME /home/siriususer  
  
# Add the needed packages for JBDS  
RUN dnf -y update \  
&& dnf -y install \  
gettext \  
gtk3 \  
zip \  
unzip \  
java-1.8.0-openjdk-devel \  
liberation-sans-fonts \  
webkitgtk3 \  
maven \  
nss_wrapper \  
openbox \  
tigervnc-server \  
wmctrl \  
origin-clients \  
&& dnf -y clean all  
  
# Create installation directory and set the openbox window manager  
# configuration for all users  
RUN mkdir -p /usr/share/sirius \  
&& echo 'export DISPLAY=:1' >> /etc/xdg/openbox/environment \  
&& echo "/usr/share/sirius/ObeoDesigner-Community/obeodesigner -nosplash -data
${HOME}/workspace &" \  
>> /etc/xdg/openbox/autostart  
  
# Add the installation configuration file  
ADD resources/InstallConfigRecord.xml /usr/share/sirius/  
ADD resources/family_updatesite /usr/share/sirius/family_updatesite  
  
# Install Sirius. The needed files will be downloaded  
# from the provided URL. The reason for this is to not include the  
# JBDS distribution in the docker layer since this image is going to  
# be quite large. If the docker ADD instruction is used the file  
# becomes a permanent part of that layer, bloating the size of an  
# already large image.  
#  
# THe last comand unzips the file  
#  
RUN mkdir -p /tmp/resources \  
&& cd /tmp/resources \  
&& curl -L -o ObeoDesigner-Community-10.0-linux.gtk.x86_64.zip
http://www.obeo.fr/download/release/designer/10.0/community/latest/packages/ObeoDesigner-
Community-10.0-linux.gtk.x86_64.zip \  
&& unzip ObeoDesigner-Community-10.0-linux.gtk.x86_64.zip -d /usr/share/sirius
\  
&& cd /usr/share/sirius \  
&& /usr/share/sirius/ObeoDesigner-Community/obeodesigner \  
-clean -purgeHistory \  
-application org.eclipse.equinox.p2.director \  
-noSplash \  
-repository file:/usr/share/sirius/family_updatesite/ \  
-i family_feature.feature.group \  
&& rm -fr /tmp/resources  
  
# This script starts and cleanly shuts down Sirius and the Xvnc server  
ADD resources/start.sh /usr/local/bin/  
  
# This file is used to create a temporary passwd file for use by  
# the NSS wrapper so that the openbox window manager can launch  
# correctly. OCP will use a non-deterministic user id, so we have  
# to provide a valid passwd entry for that UID for openbox  
ADD resources/passwd.template /usr/local/share/  
  
# Create the home directory and set permissions  
RUN mkdir -p ${HOME} \  
&& chmod a+rwX ${HOME} \  
&& chmod a+rx /usr/local/bin/start.sh \  
&& chmod a+r /usr/local/share/passwd.template  
  
RUN mkdir -p /projects && \  
chgrp -R 0 /projects && \  
chmod -R g+rwX /projects  
  
EXPOSE 5901  
  
USER 1000  
  
CMD /usr/local/bin/start.sh  
  
# No volume support yet, so everything in /home/siriususer is ephemeral.  
# Eventually this can be a mounted persistent volume so each user can  
# have a persistent maven repository, workspace, etc.  

