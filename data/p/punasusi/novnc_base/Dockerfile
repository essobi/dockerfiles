# Used to build an headless vnc image based on Centos  
FROM centos:7  
MAINTAINER Andy Allred "andy@punasusi.com"  
ENV DISPLAY=:1 \  
VNC_PORT=5901 \  
NO_VNC_PORT=8888  
EXPOSE $NO_VNC_PORT  
  
### Envrionment config  
ENV HOME=/headless \  
TERM=xterm \  
STARTUPDIR=/dockerstartup \  
INST_SCRIPTS=/headless/install \  
NO_VNC_HOME=/headless/noVNC \  
VNC_COL_DEPTH=24 \  
VNC_RESOLUTION=1580x900 \  
VNC_PW=punasusi \  
VNC_VIEW_ONLY=false  
WORKDIR $HOME  
  
### Add all install scripts for further steps  
ADD ./src/install/ $INST_SCRIPTS/  
RUN find $INST_SCRIPTS -name '*.sh' -exec chmod a+x {} +  
  
### Install some common tools  
RUN $INST_SCRIPTS/tools.sh  
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'  
### Install xvnc-server & noVNC - HTML5 based VNC viewer  
RUN $INST_SCRIPTS/tigervnc.sh  
RUN $INST_SCRIPTS/no_vnc.sh  
  
### Install firefox and chrome browser  
RUN $INST_SCRIPTS/firefox.sh  
RUN $INST_SCRIPTS/chrome.sh  
  
### Install xfce UI  
RUN $INST_SCRIPTS/xfce_ui.sh  
ADD ./src/xfce/ $HOME/  
  
### configure startup  
RUN $INST_SCRIPTS/libnss_wrapper.sh  
ADD ./src/scripts $STARTUPDIR  
RUN $INST_SCRIPTS/set_user_permission.sh $STARTUPDIR $HOME  
RUN yum clean all  
RUN cp /headless/Desktop/chromium-browser.desktop /etc/xdg/autostart/chromium-
browser.desktop  
  
ENTRYPOINT ["/dockerstartup/vnc_startup.sh"]  
CMD ["--tail-log"]  

