FROM ubuntu:rolling  
ENV DISPLAY=:2 APP_DIR=/srv  
RUN apt update && \  
DEBIAN_FRONTEND=noninteractive apt install -y x11-xserver-utils spice-vdagent
xserver-xorg-video-qxl xserver-xspice git openbox xterm x11-xkb-utils wget
unzip  
RUN cd $APP_DIR && \  
git clone https://github.com/andreasreinhardt/spice-web-client spice-web-
client && \  
git clone https://github.com/kanaka/websockify websockify  
  
ENV INSPECTIT_VERSION 1.8.2.96  
# download the inspectIT UI  
RUN wget
https://github.com/inspectIT/inspectIT/releases/download/${INSPECTIT_VERSION}/inspectit-
linux.gtk.x86_64-${INSPECTIT_VERSION}.zip -O /opt/inspectit.zip \  
&& unzip /opt/inspectit.zip \  
&& rm /opt/inspectit.zip  
RUN apt install -y libgtk2.0-0 libxtst6  
RUN apt install -y ratpoison  
  
# disable showing of welcome screen  
RUN mkdir -p
/inspectit/workspace/.metadata/.plugins/org.eclipse.core.runtime/.settings/ \  
&& printf "eclipse.preferences.version=1\nshowIntro=false\n" >
/inspectit/workspace/.metadata/.plugins/org.eclipse.core.runtime/.settings/org.eclipse.ui.prefs  
  
# preconfigure CMR  
COPY ui.prefs /inspectit/configuration/.settings/rocks.inspectit.ui.rcp.prefs  
  
COPY ratpoisonrc /root/.ratpoisonrc  
  
WORKDIR /inspectit  
EXPOSE 5900 6080  
COPY run.sh /  
CMD /run.sh

