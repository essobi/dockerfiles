FROM area51/java:jdk-8  
MAINTAINER Peter Mount <peter@retep.org>  
  
RUN apk add --update \  
sudo \  
libxext-dev \  
libxrender-dev \  
libxtst-dev &&\  
rm -rf /var/cache/apk/*  
  
# Using local copy as zip is big  
#COPY netbeans-8.1-201510222201.zip /tmp/  
#RUN cd /opt;unzip -q /tmp/netbeans-8.1-201510222201.zip &&\  
# echo "netbeans_jdkhome=\"/opt/jdk\"" >>/opt/netbeans/etc/netbeans.conf  
# Retrieve download  
RUN curl -jkL \  
-o /tmp/netbeans-8.1-201510222201.zip \  
http://download.netbeans.org/netbeans/8.1/final/zip/netbeans-8.1-201510222201.zip
&&\  
cd /opt;unzip -q /tmp/netbeans-8.1-201510222201.zip &&\  
echo "netbeans_jdkhome=\"/opt/jdk\"" >>/opt/netbeans/etc/netbeans.conf &&\  
rm -f /tmp/netbeans*  
  
RUN addgroup -g 1000 user &&\  
adduser -h /home/user \  
-u 1000 \  
-G user \  
-s /bin/ash \  
-D user &&\  
echo "user:user" | chpasswd &&\  
mkdir -p /home/user &&\  
chown user:user /home/user &&\  
echo "user ALL=(ALL) NOPASSWD: ALL" >>/etc/sudoers  
  
USER user  
CMD ["/opt/netbeans/bin/netbeans"]  
  
# Mount this to the same location to mount to the local X11 server  
VOLUME /tmp/.X11-unix  
  
# The user's home directory, mount to a volume to persist everything  
# i.e. browser history etc  
WORKDIR /home/user  
VOLUME /home/user  

