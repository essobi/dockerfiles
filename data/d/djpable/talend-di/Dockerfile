FROM kaixhin/vnc  
  
RUN apt-get -y update && \  
apt-get -y upgrade && \  
apt-get install -y software-properties-common unzip  
  
# Java installation  
RUN apt-add-repository -y ppa:webupd8team/java && \  
apt-get -y update && \  
yes | apt-get install -y oracle-java8-installer  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
#export PATH=$JAVA_HOME/bin:$PATH #NON SERVE  
# Install xulrunner from Mozilla  
#cd /opt  
#FFVER=`grep -Po "\d{2}\\.\d+" /usr/lib/firefox/platform.ini`  
#ARCH=`uname -p`  
#XURL=https://ftp.mozilla.org/pub/mozilla.org/xulrunner/releases/$FFVER/runtimes/xulrunner-$FFVER.en-
US.linux-$ARCH.tar.bz2  
#cd /opt  
#sudo sh -c "wget -O- $XURL | tar -xj"  
#sudo ln -s /opt/xulrunner/xulrunner /usr/bin/xulrunner  
#sudo ln -s /opt/xulrunner/xpcshell /usr/bin/xpcshell  
ADD files/xulrunner-1.9.2.28pre.en-US.linux-x86_64.tar.bz2 /opt/  
RUN ln -s /opt/xulrunner/xulrunner /usr/bin/xulrunner  
  
# Install Talend Open Studio for Data Integration  
ADD files/TOS_DI-20150908_1633-V6.0.1.zip /opt/  
RUN unzip /opt/TOS_DI-20150908_1633-V6.0.1.zip -d /opt && \  
rm /opt/TOS_DI-20150908_1633-V6.0.1.zip && \  
mv /opt/TOS_DI-20150908_1633-V6.0.1 /opt/tos_di && \  
chmod +x /opt/tos_di/TOS_DI-linux-gtk-x86  
  
# /usr/share/applications/talend_di.desktop

