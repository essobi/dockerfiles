from centos:6  
  
RUN yum install -y wget git  
#RUN wget http://packages.sw.be/rpmforge-release/rpmforge-
release-0.5.2-2.el6.rf.i686.rpm  
#RUN rpm -ivh rpmforge-release-0.5.2-2.el6.rf.i686.rpm  
  
RUN wget http://download.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
RUN rpm -ivh epel-release-6-8.noarch.rpm  
  
RUN yum -y install p7zip mediainfo  
RUN cd /opt; git clone https://github.com/dagon666/napi.git  
RUN cd /opt/napi; ./install.sh  
  
  
ENV SLEEP 3h  
#ENV OPTIONS "-d -s -f subrip -C UTF-8 -a pl"  
  
#ENV PGID 1001  
#ENV PUID 1001  
  
  
#RUN groupadd -g $PGID media && \  
# useradd -u $PUID -g $PGID media  
#groupadd -g $PGID media  
#useradd -u $PUID -g $PGID media  
#su - media  
COPY perm.sh /opt/  
COPY start.sh /opt/  
  
#RUN chown media:media /opt/start.sh  
RUN chmod +x /opt/start.sh  
RUN chmod +x /opt/perm.sh  
  
VOLUME /mnt/storage  
#USER media  
  
WORKDIR /opt/  
ENTRYPOINT ./start.sh  
  
LABEL org.freenas.interactive="false" \  
org.freenas.version=1 \  
org.freenas.autostart="true" \  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/mnt/storage\", \  
\"descr\": \"Media folder\" \  
} \  
]" \  
org.freenas.settings="[ \  
{ \  
\"env\": \"OPTIONS\", \  
\"descr\": \"Options for napi.sh(example:-d -s -f subrip -C UTF-8 -a pl)\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"PGID\", \  
\"descr\": \"GroupID\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"PUID\", \  
\"descr\": \"UserID\", \  
\"optional\": true \  
} \  
]"  

