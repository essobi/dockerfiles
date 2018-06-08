FROM debian:jessie  
  
MAINTAINER Alisson Pereira dos Santos <lissonpsantos2@gmail.com>, Denisson
Leal <denissonleal@gmail.com>, Geidson Benicio <geidsonc@gmail.com>  
  
#CREATE PEC 2.2.15 FOLDER  
RUN mkdir /home/PEC  
  
#SET WORKDIR PEC 2.2.15 FOLDER  
WORKDIR /home/PEC  
  
#UPDATE IMAGE  
RUN apt-get update  
RUN apt-get upgrade -y  
  
#INSTALL PACKAGES  
RUN apt-get install -y wget \  
openjdk-7-jdk \  
nano \  
vim \  
git \  
sudo \  
htop \  
curl \  
bash-completion \  
unzip  
  
#PEC INSTALL  
RUN wget
http://189.28.128.100/dab/docs/portaldab/aplicativos/Instalador_eSUS_AB_PEC_Linux_Treinamento_2_2_15_21122017.zip  
RUN unzip Instalador_eSUS_AB_PEC_Linux_Treinamento_2_2_15_21122017.zip -d
/home/PEC/install  
WORKDIR /home/PEC/install  
  
#ENV VARIABLES  
ENV PATH /sbin:$PATH  
ENV PATH /bin:$PATH  
ENV PATH /usr/sbin:$PATH  
ENV PATH /usr/bin:$PATH  
ENV PATH /usr/local/sbin:$PATH  
ENV PATH /usr/local/bin:$PATH  
  
#BASHRC STYLE  
RUN curl -o /root/.bashrc
https://raw.githubusercontent.com/lissonpsantos2/dockerfiles/master/debian-
PEC2.2.15/bashrc #redo  
  
#LOCALE PT_BR  
RUN curl -o /etc/locale.gen
https://raw.githubusercontent.com/lissonpsantos2/dockerfiles/master/debian-
PEC2.2.15/locale #redo  
  
#JAVA.CONF FILE  
RUN curl -o /etc/java.conf
https://raw.githubusercontent.com/lissonpsantos2/dockerfiles/master/debian-
PEC2.2.15/javaconf #redo  
  
RUN apt-get install -y locales  
RUN locale-gen  
RUN sh instalador_linux.sh  
  
WORKDIR /  

