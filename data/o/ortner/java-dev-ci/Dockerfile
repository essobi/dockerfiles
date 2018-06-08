FROM ubuntu:16.04  
#RUN apt-get -y install openjdk-8-jdk && \  
#RUN apt-get -y install xvfb x11vnc twm xterm  
#RUN apt-get -y install vnc4server twm  
  
  
RUN echo "### Init base functionality of ubuntu ###" && \  
set -xe && \  
apt-get -y update && \  
locale-gen en_US.UTF-8 && \  
locale-gen de_DE.UTF-8 && \  
export LANG=en_US.UTF-8 && \  
echo "### setting up window server for GUI tests ###" && \  
apt-get -y --no-install-recommends install xvfb libgtk2.0-0 libxtst6 && \  
echo "### installing java ###" && \  
apt-get -y --no-install-recommends install apt-utils software-properties-
common && \  
add-apt-repository ppa:webupd8team/java && \  
apt-get -y update && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get -y --no-install-recommends install oracle-java8-installer oracle-
java8-set-default && \  
echo "# Strip down java a bit #" && \  
rm -f /usr/lib/jvm/java-8-oracle/*src.zip && \  
rm -rf /usr/lib/jvm/java-8-oracle/lib/missioncontrol && \  
rm -rf /usr/lib/jvm/java-8-oracle/lib/visualvm && \  
apt-get -y remove apt-utils software-properties-common && \  
echo "### installing developer tools ###" && \  
apt-get -y --no-install-recommends install gradle git maven nano && \  
echo "### setting up environment ###" && \  
wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.2.0/dumb-init_1.2.0_amd64 && \  
chmod +x /usr/local/bin/dumb-init && \  
echo "### Clean up ###" && \  
apt-get -y autoremove && \  
apt-get clean && \  
rm -rf /var/cache/* && \  
rm -rf /var/tmp/* && \  
rm -rf /var/log/* && \  
rm -rf /tmp/*  
  
#configuring environment  
#use docker run —env activeJava=<value> to override the active java version  
ENV HOME=/home/work \  
scriptdir=/home/script \  
IS_CONTAINER=true \  
activeJava=java-8-oracle \  
PATH=/home/dev/bin:${PATH}  
  
ADD *.sh $scriptdir/  
## TODO COPY and ADD do not support user currently. This increases layer
size...  
COPY home $HOME/  
#Configuring user  
RUN useradd work && chown -R work: $HOME  
WORKDIR $HOME  
USER work  
  
#Setting initial state  
#CMD dumb-init bash --init-file $scriptdir/init.sh -s  
ENTRYPOINT dumb-init bash -C $scriptdir/init.sh  
  

