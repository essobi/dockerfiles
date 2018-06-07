############################################  
#From: os source  
#  
#Description:  
#  
#Version 0.0.9  
#  
###########################################  
  
FROM ubuntu:latest  
MAINTAINER Philippe "philippe.bazerbe@laposte.net"  
  
#Depots, mises a jour et install  
RUN apt-get install -y --no-install-recommends software-properties-common  
RUN add-apt-repository ppa:x2go/stable -y  
  
RUN apt-get update && \  
apt-get upgrade -y -q && \  
apt-get dist-upgrade -y -q && \  
apt-get -y -q autoclean && \  
apt-get -y -q autoremove  
  
ENV DEBIAN_FRONTEND noninteractive  
  
#################################################################  
########### partie installation ##########  
#  
#  
#  
  
# Partie 1: les softs principaux  
#Installation de x2go  
#RUN apt-get -y -q install xserver-xephyr  
#RUN add-apt-repository ppa:x2go/stable -y  
RUN apt-get -y -q install openssh-server xserver-xephyr  
#RUN apt-get -y -q install xubuntu-desktop  
RUN apt-get -y -q install xfce4 \  
gtk3-engines-xfce \  
xfce4-goodies \  
xfwm4-themes \  
ppa-purge \  
gksu \  
gedit  
  
RUN apt-get install -y -q x2goserver \  
x2goserver-xsession \  
pwgen  
  
# PArtie 2 tout ce qui est optionnel  
RUN apt-get install -y -q locate \  
ssh \  
curl \  
ntp  
  
RUN apt-get install -y -q gnome-icon-theme-full \  
tango-icon-theme  
  
RUN apt-get install -y -q firefox  
########## Tout ce qui concerne la configuration ############  
#Partie 1 les users unix  
RUN localedef -v -c -i fr_FR -f UTF-8 ISO_8859-1:1987 || :  
# Création des users nécéssaires  
RUN useradd -m kluster -s /bin/bash  
  
  
# Partie 2 configuration  
  
# configuration user  
RUN adduser kluster sudo  
RUN echo 'kluster:pass' | chpasswd  
  
#correction pb DBUs  
RUN dpkg-divert --local --rename --add /sbin/initctl && \  
ln -sf /bin/true /sbin/initctl  
  
  
# partie 3 on construit les fichiers de parametre  
  
#répertoire ou je vais etre quand je vais me connecter  
WORKDIR /home/user/  
  
  
#Shinken ecoute sur le port 5000  
EXPOSE 22  
  
#Démarrage des services  
#CMD ["/usr/sbin/sshd", "-D"]  
CMD ["/etc/init.d/ssh", "start"]  

