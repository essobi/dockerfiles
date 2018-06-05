# Dockerfile para la creacion de un ubuntu NOVNC con escritorio Unity  
FROM ubuntu:16.04  
MAINTAINER Javi Javier  
  
# Variables para nombre de Usuario.  
ENV DEBIAN_FRONTEND noninteractive  
ENV USER ubuntu  
ENV HOME /home/$USER  
# Crear nuevo usuario para iniciar sesión en NOVNC.  
RUN adduser $USER \--disabled-password  
  
# Instalar Ubuntu con escritorio Unity.  
RUN apt-get update \  
&& apt-get install -y \  
ubuntu-desktop \  
unity-lens-applications \  
gnome-panel \  
metacity \  
nautilus \  
gedit \  
xterm \  
sudo  
  
# Instalar paquetes.  
RUN apt-get install -y \  
supervisor \  
net-tools \  
curl \  
git \  
pwgen \  
libtasn1-3-bin \  
libglu1-mesa \  
&& apt-get autoclean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/*  
  
# Copiar tigerVNC-1.8.0.X86_64.  
ADD tigervnc-1.8.0.x86_64 /  
  
# Clonar NOVNC.  
RUN git clone https://github.com/novnc/noVNC.git $HOME/noVNC  
  
# Clonar Websockify.  
Run git clone https://github.com/kanaka/websockify
$HOME/noVNC/utils/websockify  
  
# Descargar NGROK.  
ADD https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
$HOME/ngrok/ngrok.zip  
RUN unzip -o $HOME/ngrok/ngrok.zip -d $HOME/ngrok && rm $HOME/ngrok/ngrok.zip  
  
# Copiar Supervisor.conf  
COPY supervisor.conf /etc/supervisor/conf.d/  
  
# Iniciar session con el escritorio Unity.  
COPY xsession $HOME/.xsession  
  
# Copiar Startup.sh  
COPY startup.sh $HOME  
  
# Exponer puertos 6080 5901 4040  
EXPOSE 6080 5901 4040  
CMD ["/bin/bash", "/home/ubuntu/startup.sh"]  

