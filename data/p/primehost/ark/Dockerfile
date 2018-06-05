FROM primehost/steam  
MAINTAINER Prime-Host <info@nordloh-webdesign.de>  
  
# update before install  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# Var for first config  
# Server Name  
ENV SESSIONNAME "Ark Docker"  
# Map name  
ENV SERVERMAP "TheCenter"  
# Server password  
ENV SERVERPASSWORD ""  
# Admin password  
ENV ADMINPASSWORD "adminpassword"  
# Nb Players  
ENV NBPLAYERS 200  
# If the server is updating when start with docker start  
ENV UPDATEONSTART 1  
# if the server is backup when start with docker start  
ENV BACKUPONSTART 0  
# Server PORT (you can't remap with docker, it doesn't work)  
ENV SERVERPORT 27015  
# Steam port (you can't remap with docker, it doesn't work)  
ENV STEAMPORT 7778  
# if the server should backup after stopping  
ENV BACKUPONSTOP 0  
# If the server warn the players before stopping  
ENV WARNONSTOP 0  
# UID of the user steam  
ENV UID 1000  
# GID of the user steam  
ENV GID 1000  
# Copy & rights to folders  
COPY run.sh /home/steam/run.sh  
COPY user.sh /home/steam/user.sh  
COPY crontab /home/steam/crontab  
COPY arkmanager-user.cfg /home/steam/arkmanager.cfg  
  
RUN touch /root/.bash_profile  
RUN chmod 777 /home/steam/run.sh  
RUN chmod 777 /home/steam/user.sh  
RUN mkdir /ark  
  
# We use the git method, because api github has a limit ;)  
RUN git clone https://github.com/FezVrasta/ark-server-tools.git
/home/steam/ark-server-tools  
WORKDIR /home/steam/ark-server-tools/  
# Install  
WORKDIR /home/steam/ark-server-tools/tools  
RUN chmod +x install.sh  
RUN ./install.sh steam  
  
# Allow crontab to call arkmanager  
RUN ln -s /usr/local/bin/arkmanager /usr/bin/arkmanager  
  
# Define default config file in /etc/arkmanager  
COPY arkmanager-system.cfg /etc/arkmanager/arkmanager.cfg  
  
# Define default config file in /etc/arkmanager  
COPY instance.cfg /etc/arkmanager/instances/main.cfg  
  
RUN chown steam -R /ark && chmod 755 -R /ark  
  
EXPOSE ${STEAMPORT} 32330 ${SERVERPORT}  
# Add UDP  
EXPOSE ${STEAMPORT}/udp ${SERVERPORT}/udp  
  
VOLUME /ark  
  
# Change the working directory to /arkd  
WORKDIR /ark  
  
# Update game launch the game.  
ENTRYPOINT ["/home/steam/user.sh"]  

