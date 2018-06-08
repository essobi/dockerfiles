FROM ubuntu:14.04  
MAINTAINER Quentin Perez "quentinperez70150@gmail.com"  
ARG
URL_ECLIPSE=http://mirror.ibcp.fr/pub/eclipse//technology/epp/downloads/release/oxygen/2/eclipse-
modeling-oxygen-2-linux-gtk-x86_64.tar.gz  
  
################## BEGIN INSTALLATION ######################  
RUN sed 's/main$/main universe/' -i /etc/apt/sources.list && \  
apt-get update && apt-get install -y software-properties-common && \  
add-apt-repository ppa:webupd8team/java -y && \  
apt-get update && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java8-installer libxext-dev libxrender-dev libxtst-
dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
# Install libgtk as a separate step  
RUN apt-get update && apt-get install -y libgtk2.0-0 libcanberra-gtk-module  
  
#Install from tmp with the script build_install_eclipse.sh  
ADD ./build_install_eclipse.sh /tmp  
ADD $URL_ECLIPSE /tmp  
RUN echo 'Run script to install eclipse' && \  
cd /tmp && \  
chmod +x ./build_install_eclipse.sh && \  
sync && \  
./build_install_eclipse.sh $URL_ECLIPSE  
  
#Install ATL, Accelo and Papyrus Plugins  
RUN cd /opt/eclipse && \  
./eclipse -application org.eclipse.equinox.p2.director -repository
http://download.eclipse.org/releases/oxygen/ -installIU
org.eclipse.acceleo.feature.group && \  
./eclipse -application org.eclipse.equinox.p2.director -repository
http://download.eclipse.org/releases/oxygen/ -installIU
org.eclipse.m2m.atl.feature.group && \  
./eclipse -application org.eclipse.equinox.p2.director -repository
http://download.eclipse.org/modeling/mdt/papyrus/updates/releases/oxygen,http://download.eclipse.org/modeling/mdt/papyrus/components/bpmn/oxygen,http://download.eclipse.org/modeling/mdt/papyrus/components/sysml14/oxygen,http://download.eclipse.org/releases/oxygen
-installIU
org.eclipse.papyrus.sdk.feature.feature.group,org.eclipse.papyrus.toolsmiths.feature.feature.group,org.eclipse.papyrus.sysml14.feature.feature.group,org.eclipse.papyrus.bpmn.feature.feature.group  
  
#Set rights for user : developer  
RUN chown -R 1000:1000 /opt/eclipse  
RUN chmod +x /opt/eclipse && \  
mkdir -p /home/developer && \  
echo "developer:x:1000:1000:Developer,,,:/home/developer:/bin/bash" >>
/etc/passwd && \  
echo "developer:x:1000:" >> /etc/group && \  
echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \  
chmod 0440 /etc/sudoers.d/developer && \  
chown developer:developer -R /home/developer && \  
chown -R developer:developer /opt/eclipse && \  
chown root:root /usr/bin/sudo && chmod 4755 /usr/bin/sudo  
################### END INSTALLATION ######################  
  
############# BEGIN SET PARAMS FOR STARTUP ################  
USER developer  
ENV HOME /home/developer  
WORKDIR /home/developer  
  
CMD /opt/eclipse/eclipse  
############## END SET PARAMS FOR STARTUP #################  

