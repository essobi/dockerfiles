FROM ubuntu:16.04  
MAINTAINER Steyn Geldenhuys "steyn@truevolve.technology"  
ENV GRADLE_FOLDER /home/developer/.gradle  
  
RUN sed 's/main$/main universe/' -i /etc/apt/sources.list  
RUN \  
apt-get update && \  
apt-get remove -y openjdk* && \  
apt-get install -y software-properties-common apt-transport-https wget && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
wget -q -O - wget https://dl.winehq.org/wine-builds/Release.key | apt-key add
- && \  
apt-add-repository 'https://dl.winehq.org/wine-builds/ubuntu/' && \  
dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get install -y software-properties-common libxext-dev libxrender-dev
libxtst-dev* x11-apps git sudo oracle-java8-set-default wine-stable-amd64
winehq-stable dpkg-dev fakeroot lintian curl wget \  
build-essential cmake libssh2-1-dev maven && \  
apt-get dist-upgrade -y && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
RUN mkdir -p /home/developer/ && \  
echo "developer:x:1000:1000:Developer,,,:/home/developer:/bin/bash" >>
/etc/passwd && \  
echo "developer:x:1000:" >> /etc/group && \  
echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \  
chmod 0440 /etc/sudoers.d/developer && \  
chown developer:developer -R /home/developer  
  
USER developer  
  
RUN mkdir ${GRADLE_FOLDER}  
RUN echo "allprojects {\n repositories {\n mavenLocal()\n maven {\n
credentials {\n username travenUser\n password travenPassword\n\  
}\n url \"https://truevolve-traven.appspot.com\"\n }\n }\n}\n" >
${GRADLE_FOLDER}/init.gradle  
  
RUN echo
"travenUser=REPLACE_THIS_WITH_YOUR_USERNAME\ntravenPassword=REPLACE_THIS_WITH_YOUR_PASSWORD\norg.gradle.caching=true"
> ${GRADLE_FOLDER}/gradle.properties  
  
RUN mkdir /home/developer/wine64  
ADD wine64 /home/developer/wine64  
RUN sudo chmod -R 0777 /home/developer/wine64/  
  
RUN mkdir /home/developer/wine32  
ADD wine32 /home/developer/wine32  
RUN sudo chmod -R 0777 /home/developer/wine32/  
  
ENV HOME /home/developer  
WORKDIR /home/developer  
CMD /bin/bash  

