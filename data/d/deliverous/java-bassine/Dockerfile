from deliverous/common-bassine  
run apt-get update && \  
apt-get install -y x11vnc xvfb &&\  
apt-get clean  
  
run apt-get update && \  
apt-get install -y openjdk-7-jdk eclipse maven &&\  
apt-get clean  
  
run apt-get update && \  
apt-get install -y ratpoison xterm &&\  
apt-get clean  
  
#add https://download.jetbrains.com/idea/ideaIC-15.0.1.tar.gz
/usr/local/share/  
user pierre  
workdir /home/pierre  
run mkdir ~/.vnc  
env FD_PROG /usr/bin/ratpoison  
env X11VNC_FINDDISPLAY_ALWAYS_FAILS 1  
env X11VNC_CREATE_GEOM 1280x768x16  
run echo "exec /usr/bin/eclipse" > ~/.ratpoisonrc  
expose 5900  
cmd x11vnc -storepasswd $VNC_PWD ~/.vnc/passwd; x11vnc -forever -usepw -create
-shared  

