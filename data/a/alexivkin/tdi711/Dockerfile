FROM scratch  
  
MAINTAINER alexivkin  
  
ADD SLES_11_SP4_JeOS.x86_64.tar.gz /  
ADD TDI_IDENTITY_E_V7.1.1_LIN-X86-64(CZUF3ML).tar /tmp/tdi/  
ADD 7.1.1-TIV-TDI-FP0005.zip /tmp/tdi/  
ADD tdi_respfile711.txt /tmp/tdi/  
  
ARG USER_ID=0  
ARG GROUP_ID=0  
  
# TODO it may be better to move all the shell code into a configuration script
and run it in one swoop, since every RUN action creates/removes a temporary
container  
# also you can handle errors better in a config script  
# match developer UID/GID to the user building the image, so that X and the
volume mapping would work  
RUN if [[ $(id -g developer) -ne $GROUP_ID ]]; then groupmod -g $GROUP_ID
users; usermod -g $GROUP_ID developer; chown -R :$GROUP_ID /home/developer; fi  
RUN if [[ $(id -u developer) -ne $USER_ID ]]; then usermod -u $USER_ID
developer; chown -R $USER_ID /home/developer; fi  
RUN id -g developer  
RUN grep user /etc/group  
  
# install TDI. exit with 0 to swallow "cant find KDE or GNOME" errors  
RUN /tmp/tdi/linux_x86_64/install_tdiv711_linux_x86_64.bin -f
"/tmp/tdi/tdi_respfile711.txt" -i silent; exit 0  
# get the latest fixpack on  
RUN unzip /tmp/tdi/7.1.1-TIV-TDI-FP0005.zip -d /tmp/tdi/  
RUN cp /tmp/tdi/7.1.1-TIV-TDI-FP0005/UpdateInstaller.jar
/opt/IBM/TDI/V7.1.1/maintenance/  
RUN /opt/IBM/TDI/V7.1.1/bin/applyUpdates.sh -update /tmp/tdi/7.1.1-TIV-TDI-
FP0005/TDI-7.1.1-FP0005.zip  
# install RMI dispatcher so we can run ISIM adapters  
# /opt/IBM/TDI/V7.1.1/jvm/jre/bin/java -jar DispatcherInstall.jar -i silent
-DUSER_SELECTED_SOLDIR="/home/developer/"  
# other silent options: -DUSER_INSTALL_DIR="/opt/IBM/TDI/V7.1"
-DUSER_INPUT_RMI_PORTNUMBER=1099 -DUSER_INPUT_WS_PORTNUMBER=8081  
# cleanup  
RUN rm -rf /tmp/tdi /opt/IBM/TDI/V7.1.1/maintenance/BACKUP  
# keep /opt/IBM/TDI/V7.1.1/docs  
# Remove boot, as it's not used in Docker. The base cleanup has to be done
there, not during the OS img2tgz conversion since the raw disk is read only.  
RUN rm -rf tmp/boot  
  
# make it pretty  
ENV GTK2_RC_FILES=/usr/share/themes/Clearlooks/gtk-2.0/gtkrc  
  
USER developer  
WORKDIR /home/developer  
  
# workspace should be mapped via a volume  
CMD /opt/IBM/TDI/V7.1.1/ibmditk  

