# ssh -L 5900:localhost:5900 desktop@localhost -p 2222  
FROM cubeearth/headless-desktop:ubuntu_bionec  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y openssh-server x11vnc && \  
mkdir /var/run/sshd && \  
sudo -u desktop mkdir ~desktop/.ssh && \  
sudo -u desktop mkdir /home/desktop/.vnc && \  
sudo -i -u desktop x11vnc -storepasswd x ~desktop/.vnc/passwd  
  
RUN apt-get update && apt-get install -y websockify net-tools && \  
wget https://bootstrap.pypa.io/ez_setup.py -O - | python && \  
rm setuptools-*.zip && \  
wget https://github.com/kanaka/noVNC/archive/master.zip && \  
sudo -i -u desktop unzip $PWD/master.zip && \  
rm master.zip && \  
mv home/desktop/noVNC-master/ home/desktop/noVNC/  
  
RUN apt-get update && apt-get install -y socat && \  
echo "export CONTAINER_LABEL=remote_desktop" >> /etc/profile  
  
RUN apt-get update && apt-get install -y xdm openbox obconf obmenu fbpanel
gpick nautilus && \  
mkdir -p /home/desktop/.config/openbox /home/desktop/.local/share/applications
/home/desktop/.config/fbpanel && \  
cp /etc/xdg/openbox/rc.xml /home/desktop/.config/openbox/rc.xml && \  
cp /usr/share/fbpanel/default /usr/share/fbpanel/pager
/home/desktop/.config/fbpanel/ && \  
chown -R desktop /home/desktop/.config/ /home/desktop/.local/  
  
RUN apt-get install -y xrdp && \  
cd /etc/xrdp && xrdp-keygen xrdp  
  
# xrdp-genkeymap for switching keyboard layout??  
RUN sh -c "echo desktop:changeme | chpasswd"  
  
EXPOSE 22 3389  
COPY startwm.sh /etc/xrdp/  
  
COPY scripts/*.sh /usr/scripts/  
RUN chmod -R +x /usr/scripts  
  
COPY home/ /home/desktop/  
RUN chown -R desktop /home/desktop  
  
ENTRYPOINT [ "/usr/scripts/exec.sh" ]  

