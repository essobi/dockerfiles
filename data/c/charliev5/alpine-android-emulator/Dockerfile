FROM charliev5/alpineedge  
  
# Java Version  
ENV JAVA_VERSION_MAJOR 8  
ENV JAVA_VERSION_MINOR 45  
ENV JAVA_VERSION_BUILD 14  
ENV JAVA_PACKAGE jdk  
  
ADD apk /tmp/apk  
RUN cp /tmp/apk/-57cfc5fa.rsa.pub /etc/apk/keys  
  
RUN apk --update --no-cache add xrdp xvfb alpine-desktop xfce4 thunar-volman \  
faenza-icon-theme slim xf86-input-synaptics xf86-input-mouse xf86-input-
keyboard \  
setxkbmap sudo util-linux dbus wireshark ttf-freefont xauth supervisor
busybox-suid openssl nano \  
&& apk add /tmp/apk/ossp-uuid-1.6.2-r0.apk \  
&& apk add /tmp/apk/ossp-uuid-dev-1.6.2-r0.apk \  
&& apk add /tmp/apk/x11vnc-0.9.13-r0.apk \  
&& apk add --allow-untrusted /tmp/apk/glibc-2.21-r2.apk \  
&& rm -rf /tmp/* /var/cache/apk/*  
  
# Install cURL  
RUN apk --update add curl ca-certificates tar  
  
# Download and unarchive Java  
RUN mkdir /opt && curl -jksSLH "Cookie: oraclelicense=accept-securebackup-
cookie"\  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
\  
| tar -xzf - -C /opt &&\  
ln -s /opt/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} /opt/jdk &&\  
rm -rf /opt/jdk/*src.zip \  
/opt/jdk/lib/missioncontrol \  
/opt/jdk/lib/visualvm \  
/opt/jdk/lib/*javafx* \  
/opt/jdk/jre/lib/plugin.jar \  
/opt/jdk/jre/lib/ext/jfxrt.jar \  
/opt/jdk/jre/bin/javaws \  
/opt/jdk/jre/lib/javaws.jar \  
/opt/jdk/jre/lib/desktop \  
/opt/jdk/jre/plugin \  
/opt/jdk/jre/lib/deploy* \  
/opt/jdk/jre/lib/*javafx* \  
/opt/jdk/jre/lib/*jfx* \  
/opt/jdk/jre/lib/amd64/libdecora_sse.so \  
/opt/jdk/jre/lib/amd64/libprism_*.so \  
/opt/jdk/jre/lib/amd64/libfxplugins.so \  
/opt/jdk/jre/lib/amd64/libglass.so \  
/opt/jdk/jre/lib/amd64/libgstreamer-lite.so \  
/opt/jdk/jre/lib/amd64/libjavafx*.so \  
/opt/jdk/jre/lib/amd64/libjfx*.so  
# Set environment  
ENV JAVA_HOME /opt/jdk  
ENV PATH ${PATH}:${JAVA_HOME}/bin  
  
# Install android sdk  
RUN wget -qO- http://dl.google.com/android/android-sdk_r23-linux.tgz | \  
tar xvz -C /usr/local/ && \  
mv /usr/local/android-sdk-linux /usr/local/android-sdk && \  
chown -R root:root /usr/local/android-sdk/  
  
# Add android tools and platform tools to PATH  
ENV ANDROID_HOME /usr/local/android-sdk  
ENV PATH $PATH:$ANDROID_HOME/tools  
ENV PATH $PATH:$ANDROID_HOME/platform-tools  
  
# Install latest android tools and system images  
RUN ( sleep 4 && while [ 1 ]; do sleep 1; echo y; done ) | android update sdk
--no-ui --force -a --filter \  
platform-tool,android-19,android-21,android-22,build-tools-22.0.1,sys-
img-x86-android-19,sys-img-x86-android-21,sys-img-x86-android-22,sys-img-
armeabi-v7a-android-19,sys-img-armeabi-v7a-android-21,sys-img-
armeabi-v7a-android-22 && \  
echo "y" | android update adb  
  
# Create fake keymap file  
RUN mkdir /usr/local/android-sdk/tools/keymaps && \  
touch /usr/local/android-sdk/tools/keymaps/en-us  
  
  
ADD etc /etc  
  
RUN xrdp-keygen xrdp auto  
RUN sed -i '/TerminalServerUsers/d' /etc/xrdp/sesman.ini \  
&& sed -i '/TerminalServerAdmins/d' /etc/xrdp/sesman.ini  
  
EXPOSE 3389 22 5037 5554 5555  
#WORKDIR /home/alpine  
#USER alpine xrdp  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["/usr/bin/supervisord","-c","/etc/supervisord.conf"]  

