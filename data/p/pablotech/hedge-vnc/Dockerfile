#FROM pablotech/hedge-supervisord:latest  
FROM pablotech/hedge-ubuntu:latest  
  
# TIGHT VNC  
RUN printf "# thightvnc\n" > /etc/init/hedge-tightvnc.conf  
RUN printf "description \"thight vnc daemon\"\n\n" >> /etc/init/hedge-
tightvnc.conf  
  
RUN printf "start on (filesystem and net-device-up IFACE=lo)\n" >>
/etc/init/hedge-tightvnc.conf  
RUN printf "stop on runlevel [!2345]\n\n" >> /etc/init/hedge-tightvnc.conf  
  
RUN printf "expect fork\n" >> /etc/init/hedge-tightvnc.conf  
RUN printf "respawn\n" >> /etc/init/hedge-tightvnc.conf  
RUN printf "respawn limit 10 5\n\n" >> /etc/init/hedge-tightvnc.conf  
  
RUN printf "pre-start script\n" >> /etc/init/hedge-tightvnc.conf  
RUN printf "\t exec bash -c 'su - hedge -c "tightvncserver -geometry 800x600
-depth 16:0"'\n" >> /etc/init/hedge-tightvnc.conf  
RUN printf "end script\n" >> /etc/init/hedge-tightvnc.conf  
  
RUN printf "post-stop script\n" >> /etc/init/hedge-tightvnc.conf  
RUN printf "\t exec bash -c 'su - hedge -c "tightvncserver -kill :0"'\n" >>
/etc/init/hedge-tightvnc.conf  
RUN printf "end script\n" >> /etc/init/hedge-tightvnc.conf  
  
RUN printf "#end script\n" >> /etc/init/hedge-tightvnc.conf  
  
RUN echo "touch /home/hedge/.Xresources" >> /etc/rc.local  
  
RUN echo 'su - hedge -c "tightvncserver -geometry 800x600 -depth 16 :0"' >>
/etc/rc.local  
  
# SET PASSWORD  
RUN su - hedge -c "mkdir -p /home/hedge/.vnc/"  
RUN su - hedge -c "echo 1qaz2wsx | vncpasswd -f >/home/hedge/.vnc/passwd"  
RUN chmod 700 /home/hedge/.vnc/  
RUN chmod 600 /home/hedge/.vnc/passwd  
  
# PORTS  
# 22 ssh, 1194 vpn, 5900 tightVNC  
EXPOSE 22/tcp 1194/udp 5900/tcp  
  
CMD ["/etc/rc.local"]  
  

