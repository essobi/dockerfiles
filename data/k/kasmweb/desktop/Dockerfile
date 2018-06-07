# This Dockerfile is used to build an headles vnc image based on Ubuntu  
FROM consol/ubuntu-xfce-vnc:1.3.0  
USER root  
  
ENV DISPLAY :1  
ENV VNC_PORT 5901  
ENV NO_VNC_PORT 6901  
ENV AUDIO_PORT 4901  
ENV UPLOAD_PORT 4902  
EXPOSE $UPLOAD_PORT $NO_VNC_PORT $AUDIO_PORT  
  
ENV HOME /headless  
ENV STARTUPDIR /dockerstartup  
WORKDIR $HOME  
  
### Envrionment config  
ENV DEBIAN_FRONTEND noninteractive  
ENV NO_VNC_HOME $HOME/noVNC  
ENV INST_SCRIPTS $HOME/install  
  
ADD ./src/common/install/ $INST_SCRIPTS/  
ADD ./src/ubuntu/install/ $INST_SCRIPTS/  
  
RUN find $INST_SCRIPTS -name '*.sh' -exec chmod a+x {} +  
RUN $INST_SCRIPTS/no_vnc.sh  
RUN $INST_SCRIPTS/configure_xfce.sh  
RUN $INST_SCRIPTS/install_tools.sh  
RUN $INST_SCRIPTS/install_audio.sh  
  
RUN $INST_SCRIPTS/install_chrome.sh  
RUN $INST_SCRIPTS/install_firefox.sh  
RUN $INST_SCRIPTS/install_torbrowser.sh  
  
ADD ./src/common/install/kasm/upload_server $HOME/  
RUN $INST_SCRIPTS/install_upload_requirements.sh  
ADD ./src/common/scripts $STARTUPDIR  
RUN $INST_SCRIPTS/set_user_permission.sh $STARTUPDIR $HOME  
  
RUN rm /headless/.config/bg_sakuli.png  
RUN chown 1000:0 /headless  
  
ENTRYPOINT ["/dockerstartup/kasm_startup.sh"]  
  
USER 1000  

