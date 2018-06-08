FROM centos  
MAINTAINER Josh Wheeler <mantlepro@gmail.com>  
WORKDIR /root  
RUN yum install -y iproute ca-certificates openssl wget  
RUN wget -q https://downloads.plex.tv/plex-media-
server/1.7.5.4035-313f93718/plexmediaserver-1.7.5.4035-313f93718.x86_64.rpm &&
yum install -y plexmediaserver*.rpm && rm *.rpm  
COPY sysconfig /etc/sysconfig/PlexMediaServer  
COPY start.sh /root  
EXPOSE 32400 1900/udp 3005 5353/udp 8324 32410/udp 32412/udp 32413/udp
32414/udp 32469  
CMD ./start.sh  

