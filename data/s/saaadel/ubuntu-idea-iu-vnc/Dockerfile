FROM ubuntu:latest  
  
RUN apt-get -y update && \  
( DEBIAN_FRONTEND=noninteractive apt-get --no-install-recommends -yq install
which 2>/dev/null || true ) && \  
DEBIAN_FRONTEND=noninteractive apt-get --no-install-recommends -yq install
curl && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -jkL
https://raw.githubusercontent.com/saaadel/scripts/master/linux/apt-
get/nodejs.sh | sh -x /dev/stdin  
  
RUN curl -jkL
https://raw.githubusercontent.com/saaadel/scripts/master/linux/install/oracle-
java.sh | sh -x /dev/stdin  
  
RUN curl -jkL
https://raw.githubusercontent.com/saaadel/scripts/master/linux/install/maven.sh
| sh -x /dev/stdin  
  
RUN curl -jkL
https://raw.githubusercontent.com/saaadel/scripts/master/linux/install/gradle.sh
| sh -x /dev/stdin  
  
RUN curl -jkL
https://raw.githubusercontent.com/saaadel/scripts/master/linux/install/intellij-
idea-iu.sh | sh -x /dev/stdin  
  
RUN curl -jkL
https://raw.githubusercontent.com/saaadel/scripts/master/linux/install/tigervnc-
server.sh | sh -x /dev/stdin  
  
RUN . /etc/profile.d/java-env.sh && \  
. /etc/profile.d/maven-env.sh && \  
. /etc/profile.d/gradle-env.sh && \  
. /etc/profile.d/idea-env.sh && \  
sed -e 's!^.*gnome-session!\\. /etc/profile\\.d/java-env\\.sh\n\0!' -i
/home/user/.vnc/xstartup && \  
sed -e 's!^.*gnome-session!\\. /etc/profile\\.d/maven-env\\.sh\n\0!' -i
/home/user/.vnc/xstartup && \  
sed -e 's!^.*gnome-session!\\. /etc/profile\\.d/gradle-env\\.sh\n\0!' -i
/home/user/.vnc/xstartup && \  
sed -e 's!^.*gnome-session!\\. /etc/profile\\.d/idea-env\\.sh\n\0!' -i
/home/user/.vnc/xstartup && \  
sed -e 's!^.*gnome-session!$IDEA_HOME/bin/idea.sh \&\n\0!' -i
/home/user/.vnc/xstartup && \  
echo '\x32!/bin/sh' > ${HOME}/.dev-profile && \  
echo '. /etc/profile.d/java-env.sh' >> ${HOME}/.dev-profile && \  
echo '. /etc/profile.d/maven-env.sh' >> ${HOME}/.dev-profile && \  
echo '. /etc/profile.d/gradle-env.sh' >> ${HOME}/.dev-profile && \  
echo '. /etc/profile.d/idea-env.sh' >> ${HOME}/.dev-profile  
  
#RUN echo '. ~/.dev-profile' >> ${HOME}/.bashrc  
RUN [ ! -d /mnt/docker-volume ] && mkdir /mnt/docker-volume  
VOLUME /mnt/docker-volume  
EXPOSE 5901  
LABEL io.openshift.expose-services="5901:tcp"  
# USER ${USER}  
USER user  
ENV USER=user HOME=/home/user DISPLAY=":1"  
CMD []  
#ENTRYPOINT ["/usr/bin/vncserver", "-fg"]  
ENTRYPOINT rm -rf /tmp/.X11-unix/* && \  
rm -rf /tmp/.X*-lock && \  
rm -rf /tmp/*.tmp && \  
/usr/bin/vncserver -geometry "1704x900" && \  
sleep 10 && waitpid=`ps | grep X[^\s]*vnc | tail -1 | awk '{print $1; }'` && \  
sh -c "while ps -p $waitpid 1>/dev/null 2>&1; do sleep 10; done"  

