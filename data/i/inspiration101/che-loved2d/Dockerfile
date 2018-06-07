FROM eclipse/ubuntu_jre  
  
RUN sudo apt-get update && sudo apt-get install -y mesa-utils  
RUN sudo add-apt-repository ppa:bartbes/love-stable  
RUN sudo apt-get update && sudo apt-get install -y love  
  
RUN sudo apt-get update -qqy && \  
sudo apt-get -qqy install \  
supervisor \  
x11vnc \  
xvfb \  
subversion \  
net-tools \  
blackbox \  
rxvt-unicode \  
xfonts-terminus  
  
RUN sudo mkdir -p /opt/noVNC/utils/websockify  
RUN wget -qO- "http://github.com/kanaka/noVNC/tarball/master" | sudo tar -zx
--strip-components=1 -C /opt/noVNC  
RUN wget -qO- "https://github.com/kanaka/websockify/tarball/master" | sudo tar
-zx --strip-components=1 -C /opt/noVNC/utils/websockify  
RUN sudo mkdir -p /etc/X11/blackbox  
RUN echo "[begin] (Blackbox) \n [exec] (Terminal) {urxvt -fn
"xft:Terminus:size=14"} \n \  
[exec] (Love) {love} \n \  
[end]" | sudo tee -a /etc/X11/blackbox/blackbox-menu  
  
ADD index.html /opt/noVNC/  
ADD supervisord.conf /opt/  
EXPOSE 4444 6080 32745  
ENV DISPLAY :20.0  
ENV MAVEN_VERSION=3.3.9 \  
JAVA_VERSION=8u45 \  
JAVA_VERSION_PREFIX=1.8.0_45 \  
TOMCAT_HOME=/home/user/tomcat8  
  
ENV JAVA_HOME=/opt/jdk$JAVA_VERSION_PREFIX \  
M2_HOME=/home/user/apache-maven-$MAVEN_VERSION  
  
ENV PATH=$JAVA_HOME/bin:$M2_HOME/bin:$PATH  
  
RUN mkdir /home/user/cbuild /home/user/tomcat8 /home/user/apache-
maven-$MAVEN_VERSION  
RUN wget -qO- "http://apache.ip-
connect.vn.ua/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz" | tar -zx --strip-components=1 -C
/home/user/apache-maven-$MAVEN_VERSION/  
ENV TERM xterm  
  
RUN wget -qO-
"http://archive.apache.org/dist/tomcat/tomcat-8/v8.0.24/bin/apache-
tomcat-8.0.24.tar.gz" | tar -zx --strip-components=1 -C /home/user/tomcat8 &&
\  
rm -rf /home/user/tomcat8/webapps/*  
  
RUN echo "export JAVA_HOME=/opt/jdk$JAVA_VERSION_PREFIX\nexport
M2_HOME=/home/user/apache-maven-$MAVEN_VERSION\nexport
TOMCAT_HOME=/home/user/tomcat8\nexport PATH=$JAVA_HOME/bin:$M2_HOME/bin:$PATH"
>> /home/user/.bashrc && \  
sudo locale-gen en_US.UTF-8  
  
WORKDIR /projects  
  
CMD /usr/bin/supervisord -c /opt/supervisord.conf & \  
cd /home/user && sleep 3 && \  
sleep 365d  

