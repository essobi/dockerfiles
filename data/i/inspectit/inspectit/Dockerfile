FROM debian:jessie  
  
MAINTAINER info.inspectit@novatec-gmbh.de  
  
ENV INSPECTIT_VERSION 1.8.5.101  
# prepare the needed libs  
RUN apt-get update && apt-get install -y wget unzip libgtk2.0-0 libxtst6
libcanberra-gtk-module \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# download the inspectIT  
RUN wget
https://github.com/inspectIT/inspectIT/releases/download/${INSPECTIT_VERSION}/inspectit-
linux.gtk.x86_64-${INSPECTIT_VERSION}.zip -qO /opt/inspectit.zip \  
&& unzip /opt/inspectit.zip \  
&& rm /opt/inspectit.zip  
  
# disable showing of welcome screen  
RUN mkdir -p
/inspectit/workspace/.metadata/.plugins/org.eclipse.core.runtime/.settings/ \  
&& printf "eclipse.preferences.version=1\nshowIntro=false\n" >
/inspectit/workspace/.metadata/.plugins/org.eclipse.core.runtime/.settings/org.eclipse.ui.prefs  
  
CMD cd /inspectit && ./inspectIT  

