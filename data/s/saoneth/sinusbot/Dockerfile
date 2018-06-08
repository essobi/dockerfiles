FROM alpine:edge  
  
MAINTAINER Saoneth <saoneth@gmail.com>  
  
ENV TEAMSPEAK_URL
http://dl.4players.de/ts/releases/3.0.19.4/TeamSpeak3-Client-
linux_amd64-3.0.19.4.run  
ENV SINUSBOT_URL https://www.sinusbot.com/dl/sinusbot-beta.tar.bz2  
ENV TS3_UID 1001  
ENV LANG=C.UTF-8  
# Install glibc  
RUN ALPINE_GLIBC_BASE_URL="https://github.com/sgerrand/alpine-pkg-
glibc/releases/download" && \  
ALPINE_GLIBC_PACKAGE_VERSION="2.23-r3" && \  
ALPINE_GLIBC_BASE_PACKAGE_FILENAME="glibc-$ALPINE_GLIBC_PACKAGE_VERSION.apk"
&& \  
ALPINE_GLIBC_BIN_PACKAGE_FILENAME="glibc-
bin-$ALPINE_GLIBC_PACKAGE_VERSION.apk" && \  
ALPINE_GLIBC_I18N_PACKAGE_FILENAME="glibc-i18n-$ALPINE_GLIBC_PACKAGE_VERSION.apk"
&& \  
apk add --no-cache --virtual=.build-dependencies wget ca-certificates && \  
wget \  
"https://raw.githubusercontent.com/andyshinn/alpine-pkg-
glibc/master/sgerrand.rsa.pub" \  
-O "/etc/apk/keys/sgerrand.rsa.pub" && \  
wget \  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BASE_PACKAGE_FILENAME"
\  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BIN_PACKAGE_FILENAME"
\  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_I18N_PACKAGE_FILENAME"
&& \  
apk add --no-cache \  
"$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_I18N_PACKAGE_FILENAME" && \  
\  
rm "/etc/apk/keys/sgerrand.rsa.pub" && \  
/usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8
C.UTF-8 || true && \  
echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh && \  
\  
apk del glibc-i18n && \  
\  
rm "/root/.wget-hsts" && \  
apk del .build-dependencies && \  
rm \  
"$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_I18N_PACKAGE_FILENAME"  
  
# Add teamspeak user  
RUN mkdir /home/teamspeak && \  
addgroup -g ${TS3_UID} teamspeak && \  
adduser -u ${TS3_UID} -G teamspeak -h /home/teamspeak -S -D teamspeak && \  
chown -R teamspeak:teamspeak /home/teamspeak/  
  
# Install Teamspeak  
ADD $TEAMSPEAK_URL /tmp/ts3.run  
RUN sed -i 's/^MS_PrintLicense$//' /tmp/ts3.run && \  
chmod a+x /tmp/ts3.run && \  
/tmp/ts3.run && \  
rm /tmp/ts3.run && \  
mv TeamSpeak3-Client-linux_amd64 /home/teamspeak/ && \  
chown -R teamspeak:teamspeak /home/teamspeak/ && \  
apk add --no-cache xinit xvfb libxcursor glib  
  
# Install SinusBot  
ADD $SINUSBOT_URL /tmp/sinusbot.tar.bz2  
ADD run.sh /home/teamspeak/sinusbot/run.sh  
RUN tar -vxjf /tmp/sinusbot.tar.bz2 -C /home/teamspeak/sinusbot && \  
rm /tmp/sinusbot.tar.bz2 && \  
ln -s /home/teamspeak/sinusbot/plugin/libsoundbot_plugin.so
/home/teamspeak/TeamSpeak3-Client-linux_amd64/plugins/libsoundbot_plugin.so &&
\  
mv /home/teamspeak/sinusbot/config.ini.dist
/home/teamspeak/sinusbot/config.ini && \  
sed -i 's~^TS3Path = "[^"]*"$~TS3Path = "/home/teamspeak/TeamSpeak3-Client-
linux_amd64/ts3client_linux_amd64"~' /home/teamspeak/sinusbot/config.ini && \  
chmod +x /home/teamspeak/sinusbot/sinusbot && \  
# /home/teamspeak/sinusbot/sinusbot -update -RunningAsRootIsEvilAndIKnowThat
&& \  
chmod +x /home/teamspeak/sinusbot/run.sh && \  
chown -R teamspeak:teamspeak /home/teamspeak/  
  
# Add ssl support  
#WORKDIR /home/teamspeak/sinusbot  
#RUN apk add --no-cache libssl1.0  
#ADD libavformat.so.57 .  
#ADD libavcodec.so.57 .  
#ADD libavfilter.so.6 .  
#ADD libavutil.so.55 .  
#ADD libswresample.so.2 .  
#USER teamspeak  
#ENTRYPOINT ["/home/teamspeak/sinusbot/run.sh"]  
CMD /bin/sh  
  
VOLUME ["/home/teamspeak/sinusbot/data"]  
  
EXPOSE 8087  

