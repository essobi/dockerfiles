FROM alexagency/centos6-gnome  
MAINTAINER Alex  
  
USER root  
  
RUN yum -y update && \  
yum -y install xorg-x11-server-utils which prelink git wget tar bzip2 meld \  
firefox*i686 libXtst-devel.i686 gtk2.i686 gtk2-engines.i686 gtk2-devel.i686 &&
\  
yum clean all && rm -rf /tmp/* && \  
touch /var/lib/dbus/machine-id && dbus-uuidgen > /var/lib/dbus/machine-id  
  
# JDK x86  
ENV JDK_URL http://download.oracle.com/otn-
pub/java/jdk/8u65-b17/jdk-8u65-linux-i586.rpm  
RUN wget -c --no-cookies --no-check-certificate --header \  
"Cookie: oraclelicense=accept-securebackup-cookie" $JDK_URL -O jdk.rpm && \  
rpm -i jdk.rpm && rm -fv jdk.rpm  
# Firefox x86 Java plugin  
RUN alternatives --install /usr/lib/mozilla/plugins/libjavaplugin.so
libjavaplugin.so \  
/usr/java/latest/jre/lib/i386/libnpjp2.so 200000  
# Visual VM  
RUN echo -e "\  
[Desktop Entry]\n\  
Name=Visual VM\n\  
Exec=/usr/java/latest/bin/jvisualvm\n\  
Icon=gnome-panel-fish\n\  
Categories=Application;Development;Java\n\  
Type=Application\n\  
Terminal=false"\  
> /usr/share/applications/jvisualvm.desktop  
  
# Sublime Text 3  
ENV SUBLIME_URL
http://c758482.r82.cf2.rackcdn.com/sublime_text_3_build_3083_x64.tar.bz2  
RUN wget $SUBLIME_URL && \  
tar -vxjf `echo "${SUBLIME_URL##*/}"` -C /opt && \  
ln -s /opt/sublime_text_3/sublime_text /usr/bin/sublime3 && \  
rm -f `echo "${SUBLIME_URL##*/}"` && \  
echo -e "\  
[Desktop Entry]\n\  
Name=Sublime 3\n\  
Exec=sublime3\n\  
Terminal=false\n\  
Icon=/opt/sublime_text_3/Icon/48x48/sublime-text.png\n\  
Type=Application\n\  
Categories=TextEditor;IDE;Development\n\  
X-Ayatana-Desktop-Shortcuts=NewWindow\n\  
[NewWindow Shortcut Group]\n\  
Name=New Window\n\  
Exec=sublime -n\n\  
TargetEnvironment=Unity"\  
> /usr/share/applications/sublime3.desktop && \  
cp /usr/share/applications/sublime3.desktop \  
/home/user/Desktop/sublime3.desktop && \  
chown user:user /home/user/Desktop/sublime3.desktop && \  
sed -i 's\gedit.desktop\gedit.desktop;sublime3.desktop\g' \  
/usr/share/applications/defaults.list  
  
# Eclipse Luna x86  
ENV ECLIPSE_URL http://ftp-stud.fht-
esslingen.de/pub/Mirrors/eclipse/technology/epp/downloads\  
/release/mars/1/eclipse-jee-mars-1-linux-gtk.tar.gz  
RUN wget $ECLIPSE_URL && \  
tar -zxvf `echo "${ECLIPSE_URL##*/}"` -C /opt/ && \  
ln -s /opt/eclipse/eclipse /usr/bin/eclipse && \  
rm -f `echo "${ECLIPSE_URL##*/}"`  
  
# Configure profile  
RUN echo "chown user:user /home/user/Public" >> /home/user/.bashrc && \  
echo "alias install='sudo yum install'" >> /home/user/.bashrc && \  
echo "alias docker='sudo docker'" >> /home/user/.bashrc && \  
echo -e '\  
alias dockerX11run="docker run -ti --rm \  
-e DISPLAY=`hostname --ip-address`$DISPLAY" '\  
>> /home/user/.bashrc && \  
echo -e '\n\  
X64=`hostname`-x64 \n\  
X64_RUNNING=$(docker inspect -f {{.State.Running}} $X64 2> /dev/null) \n\  
if [ "$X64_RUNNING" == "true" ]; then \n\  
alias workstation-x64="docker exec -ti $X64" \n\  
else \n\  
alias workstation-x64="dockerX11run \  
\--hostname $X64 \  
\--name $X64 \  
\--link `hostname`:$X64 \  
-v /shared:/home/user/Public \  
alexagency/centos6-workstation-x64" \n\  
fi \n '\  
>> /home/user/.bashrc && \  
echo -e '\n\  
CENTOS7=`hostname`-centos7 \n\  
CENTOS7_RUNNING=$(docker inspect -f {{.State.Running}} $CENTOS7 2> /dev/null)
\n\  
if [ "$CENTOS7_RUNNING" == "true" ]; then \n\  
alias centos7="docker exec -ti $CENTOS7" \n\  
else \n\  
alias centos7="dockerX11run \  
\--hostname $CENTOS7 \  
\--name $CENTOS7 \  
\--link `hostname`:$CENTOS7 \  
-v /shared:/home/user/Public \  
alexagency/centos7-jdk-x86" \n\  
fi \n '\  
>> /home/user/.bashrc && \  
echo -e '\n\  
OPENSUSE=`hostname`-opensuse \n\  
OPENSUSE_RUNNING=$(docker inspect -f {{.State.Running}} $OPENSUSE 2>
/dev/null) \n\  
if [ "$OPENSUSE_RUNNING" == "true" ]; then \n\  
alias opensuse="docker exec -ti $OPENSUSE" \n\  
else \n\  
alias opensuse="dockerX11run \  
\--hostname $OPENSUSE \  
\--name $OPENSUSE \  
\--link `hostname`:$OPENSUSE \  
-v /shared:/home/user/Public \  
alexagency/opensuse-jdk-x86" \n\  
fi \n '\  
>> /home/user/.bashrc && \  
shopt -s expand_aliases  
  
# xhost startup script  
RUN mkdir -p /home/user/.config/autostart && \  
echo -e "\  
[Desktop Entry]\n\  
Name=xhost\n\  
Type=Application\n\  
Exec=xhost +\n\  
Hidden=false\n\  
X-GNOME-Autostart-enabled=true"\  
> /home/user/.config/autostart/xhost.desktop  
  
# Create useful links  
RUN ln -s /home/user/Public /home/user/Desktop  
  
# Terminal x64  
RUN echo -e "\  
[Desktop Entry]\n\  
Name=Workstation x64\n\  
Exec=sh -c 'source /home/user/.bashrc;eval workstation-x64 bash'\n\  
Icon=utilities-terminal\n\  
Type=Application\n\  
Terminal=true\n\  
Categories=GNOME;GTK;Utility;TerminalEmulator;System;"\  
> /usr/share/applications/terminal-x64.desktop  
  
# Terminal Centos7  
RUN echo -e "\  
[Desktop Entry]\n\  
Name=Terminal Centos7\n\  
Exec=sh -c 'source /home/user/.bashrc;eval centos7 bash'\n\  
Icon=utilities-terminal\n\  
Type=Application\n\  
Terminal=true\n\  
Categories=GNOME;GTK;Utility;TerminalEmulator;System;"\  
> /usr/share/applications/terminal-centos7.desktop  
  
# Terminal OpenSuse  
RUN echo -e "\  
[Desktop Entry]\n\  
Name=Terminal OpenSuse\n\  
Exec=sh -c 'source /home/user/.bashrc;eval opensuse bash'\n\  
Icon=utilities-terminal\n\  
Type=Application\n\  
Terminal=true\n\  
Categories=GNOME;GTK;Utility;TerminalEmulator;System;"\  
> /usr/share/applications/terminal-opensuse.desktop  
  
# Firefox x86  
RUN echo -e "\  
[Desktop Entry]\n\  
Name=Firefox\n\  
Exec=firefox %u\n\  
Icon=firefox\n\  
Terminal=false\n\  
Type=Application\n\  
Categories=Network;WebBrowser;"\  
> /usr/share/applications/firefox.desktop && \  
cp /usr/share/applications/firefox.desktop \  
/home/user/Desktop/firefox.desktop && \  
chown user:user /home/user/Desktop/firefox.desktop  
  
# Firefox x64  
RUN echo -e "\  
[Desktop Entry]\n\  
Name=Firefox x64\n\  
Exec=sh -c 'source /home/user/.bashrc;eval workstation-x64 firefox'\n\  
Icon=firefox\n\  
Terminal=true\n\  
Type=Application\n\  
Categories=Network;WebBrowser;"\  
> /usr/share/applications/firefox-x64.desktop  
  
# Firefox x86 Centos7  
RUN echo -e "\  
[Desktop Entry]\n\  
Name=Firefox Centos7\n\  
Exec=sh -c 'source /home/user/.bashrc;eval centos7 firefox'\n\  
Icon=firefox\n\  
Terminal=true\n\  
Type=Application\n\  
Categories=Network;WebBrowser;"\  
> /usr/share/applications/firefox-centos7.desktop  
  
# Firefox x86 OpenSuse  
RUN echo -e "\  
[Desktop Entry]\n\  
Name=Firefox OpenSuse\n\  
Exec=sh -c 'source /home/user/.bashrc;eval opensuse firefox'\n\  
Icon=firefox\n\  
Terminal=true\n\  
Type=Application\n\  
Categories=Network;WebBrowser;"\  
> /usr/share/applications/firefox-opensuse.desktop  
  
# Eclipse x86  
RUN echo -e "\  
[Desktop Entry]\n\  
Name=Eclipse\n\  
Exec=eclipse\n\  
Icon=/opt/eclipse/icon.xpm\n\  
Categories=Application;Development;Java;IDE\n\  
Type=Application\n\  
Terminal=false"\  
> /usr/share/applications/eclipse.desktop && \  
cp /usr/share/applications/eclipse.desktop \  
/home/user/Desktop/eclipse.desktop && \  
chown user:user /home/user/Desktop/eclipse.desktop  
  
# Eclipse x64  
RUN echo -e "\  
[Desktop Entry]\n\  
Name=Eclipse x64\n\  
Exec=sh -c 'source /home/user/.bashrc;eval workstation-x64 eclipse'\n\  
Icon=/opt/eclipse/icon.xpm\n\  
Categories=Application;Development;Java;IDE\n\  
Type=Application\n\  
Terminal=true"\  
> /usr/share/applications/eclipse-x64.desktop  
  
# Eclipse x86 Centos7  
RUN echo -e "\  
[Desktop Entry]\n\  
Name=Eclipse Centos7\n\  
Exec=sh -c 'source /home/user/.bashrc;eval centos7 eclipse'\n\  
Icon=/opt/eclipse/icon.xpm\n\  
Categories=Application;Development;Java;IDE\n\  
Type=Application\n\  
Terminal=true"\  
> /usr/share/applications/eclipse-centos7.desktop  
  
# Eclipse x86 OpenSuse  
RUN echo -e "\  
[Desktop Entry]\n\  
Name=Eclipse OpenSuse\n\  
Exec=sh -c 'source /home/user/.bashrc;eval opensuse eclipse'\n\  
Icon=/opt/eclipse/icon.xpm\n\  
Categories=Application;Development;Java;IDE\n\  
Type=Application\n\  
Terminal=true"\  
> /usr/share/applications/eclipse-opensuse.desktop  
  
# Default user  
USER user  
  
# Persist data volume  
VOLUME ["/home/user/Public"]  

