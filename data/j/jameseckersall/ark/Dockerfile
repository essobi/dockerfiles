FROM ubuntu:14.04  
MAINTAINER James Eckersall <james.eckersall@gmail.com>  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
# Var for first config  
# Server Name  
ENV \  
SESSIONNAME="Ark Docker" \  
SERVERMAP="TheIsland" \  
SERVERPASSWORD="" \  
ADMINPASSWORD="adminpassword" \  
NBPLAYERS=70 \  
UPDATEONSTART=1 \  
BACKUPONSTART=1 \  
BRANCH=master \  
SERVERPORT=27015 \  
STEAMPORT=7778  
# Install dependencies  
RUN apt-get update &&\  
apt-get install -y curl lib32gcc1 lsof git  
  
# Enable passwordless sudo for users under the "sudo" group  
RUN sed -i.bkp -e \  
's/%sudo\s\\+ALL=(ALL\\(:ALL\\)\?)\s\\+ALL/%sudo ALL=NOPASSWD:ALL/g'
/etc/sudoers \  
/etc/sudoers  
  
# Run commands as the steam user  
RUN adduser \  
\--disabled-login \  
\--shell /bin/bash \  
\--gecos "" \  
steam  
# Add to sudo group  
RUN usermod -a -G sudo steam  
  
# Copy & rights to folders  
COPY run.sh /home/steam/run.sh  
COPY crontab /home/steam/crontab  
COPY arkmanager-user.cfg /home/steam/arkmanager.cfg  
  
RUN chmod 777 /home/steam/run.sh  
RUN mkdir /ark  
  
RUN mkdir -p /home/steam/ark-server-tools  
  
# We use the git method, because api github has a limit ;)  
RUN git clone -b $BRANCH https://github.com/FezVrasta/ark-server-tools.git
/home/steam/ark-server-tools/  
# Install  
WORKDIR /home/steam/ark-server-tools/tools  
RUN chmod +x install.sh  
RUN ./install.sh steam  
  
# Allow crontab to call arkmanager  
RUN ln -s /usr/local/bin/arkmanager /usr/bin/arkmanager  
  
# Define default config file in /ark  
COPY arkmanager-system.cfg /etc/arkmanager/arkmanager.cfg  
  
RUN chown steam -R /ark && chmod 755 -R /ark  
  
USER steam  
  
# download steamcmd  
RUN mkdir /home/steam/steamcmd &&\  
cd /home/steam/steamcmd &&\  
curl http://media.steampowered.com/installer/steamcmd_linux.tar.gz | tar -vxz  
  
  
# First run is on anonymous to download the app  
RUN /home/steam/steamcmd/steamcmd.sh +login anonymous +quit  
  
EXPOSE ${STEAMPORT} 32330 ${SERVERPORT}  
  
VOLUME /ark  
  
# Change the working directory to /arkd  
WORKDIR /ark  
  
# Update game launch the game.  
ENTRYPOINT ["/home/steam/run.sh"]  

