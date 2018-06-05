FROM ubuntu:14.04  
MAINTAINER Henrik Nilsson <henrik.nilsson@bytequest.se>  
  
ENV ECLIPSE_FILE eclipse-cpp-mars-1-linux-gtk-x86_64.tar.gz  
ENV ECLIPSE_FILE_URL
http://saimei.acc.umu.se/mirror/eclipse.org/technology/epp/downloads/release/mars/1/$ECLIPSE_FILE  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
RUN apt-get update  
RUN apt-get install -yq --no-install-recommends software-properties-common  
RUN add-apt-repository ppa:webupd8team/java -y  
RUN add-apt-repository ppa:terry.guo/gcc-arm-embedded -y  
RUN apt-get update  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections  
RUN apt-get install -yq --no-install-recommends oracle-java7-installer  
RUN apt-get install -yq --no-install-recommends curl make  
RUN apt-get install -yq --no-install-recommends gcc-arm-none-eabi  
  
RUN curl -O $ECLIPSE_FILE_URL  
RUN tar -xf $ECLIPSE_FILE -C /opt  
RUN rm $ECLIPSE_FILE  
  
RUN /opt/eclipse/eclipse -nosplash -application
org.eclipse.equinox.p2.director -repository
http://gnuarmeclipse.sourceforge.net/updates/ -installIU
ilg.gnuarmeclipse.managedbuild.cross.feature.group -destination /opt/eclipse/  
  

