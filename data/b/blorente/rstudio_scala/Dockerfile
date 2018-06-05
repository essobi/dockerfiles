FROM fikovnik/rstudio  
LABEL maintainer "blorente.me@gmail.com"  
  
#RUN apt-get install -y gnupg  
# Install Java.  
RUN \  
echo "===> add webupd8 repository..." && \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee
/etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
#apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && \  
apt-get update && \  
\  
\  
echo "===> install Java" && \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes oracle-
java8-installer oracle-java8-set-default && \  
\  
\  
echo "===> clean up..." && \  
rm -rf /var/cache/oracle-jdk8-installer && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
# Ammonite  
RUN mkdir ~/.ammonite && wget -O ~/.ammonite/predef.scala https://git.io/vro0a  
RUN sudo wget -O /usr/local/bin/amm https://git.io/vASZm && chmod +x
/usr/local/bin/amm  
  
# Install tmux (for some reason it doens't come by default or with apt)  
# TODO this is extremely wrong, should use proper repos  
RUN wget -O libevent-2.0-5.deb
ftp.us.debian.org/debian/pool/main/libe/libevent/libevent-2.0-5_2.0.21-stable-3_amd64.deb  
RUN wget -O tmux_2.3.deb
ftp.us.debian.org/debian/pool/main/t/tmux/tmux_2.3-4_amd64.deb  
RUN dpkg -i libevent-2.0-5.deb  
RUN dpkg -i tmux_2.3.deb  
  
# Install R packages  
RUN Rscript -e 'install.packages("tmuxr")'  
RUN Rscript -e 'devtools::install_github("datascienceworkshops/knitractive")'  

