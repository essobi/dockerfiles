FROM debian  
MAINTAINER Jonathan Karras <jkarras@karras.net>  
  
ENV UNIFI_VERSION 3.2.2  
ENV DEBIAN_FRONTEND noninteractive  
ENV ENABLE_TMPFS no  
  
RUN apt-get update \  
&& apt-get -y dist-upgrade \  
&& apt-get -y install \  
gdebi-core \  
libtcnative-1 \  
openjdk-7-jre-headless \  
wget \  
&& apt-get -y clean  
  
#RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927 \  
# && echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/3.2 main"
| tee /etc/apt/sources.list.d/mongodb-org-3.2.list  
RUN cd /tmp \  
&& wget "http://dl.ubnt.com/firmwares/unifi-video/${UNIFI_VERSION}/unifi-
video_${UNIFI_VERSION}~Debian7_amd64.deb" \  
&& gdebi -n unifi-video_${UNIFI_VERSION}~Debian7_amd64.deb \  
&& rm -rf unifi-video_${UNIFI_VERSION}~Debian7_amd64.deb \  
&& sed -i'' 's/\\(ENABLE_TMPFS=\\).*$/\1no/' /usr/sbin/unifi-video  
  
# The following ports are used on UniFi Video hosts:  
# 1935 – RTMP streaming video to web UI & accepting gen1 camera video  
# 1935, by user (RTMP video)  
# 7443 – Controller web UI  
# 7443, by user (HTTPS), by camera (HTTPS)  
# 7080 – HTTP communication with cameras  
# 7080, by user (HTTP), by camera (HTTP)  
# 6666 – Live FLV for incoming gen2 camera streams  
# 6666, by camera (video push)  
# 7447 – RTSP re-streaming via controller  
# The following ports are used on cameras:  
# HTTP/HTTPS ports to access web interface (optional)  
# SSH to facilitate adoption by the controller on LAN (optional)  
# 554 RTSP server (mandatory only on gen1)  
EXPOSE 7447 7446 1935 7443 7080 6666  
VOLUME /var/lib/unifi-video  
VOLUME /var/log/unifi-video  
  
WORKDIR /var/lib/unifi-video  
  
#CMD ["java", "-cp", "/usr/share/java/commons-daemon.jar:/usr/lib/unifi-
video/lib/airvision.jar", "-Dav.tempdir=/var/cache/unifi-video",
"-Djava.security.egd=file:/dev/./urandom", "-Djava.awt.headless=true",
"-Dfile.encoding=UTF-8", "-Xmx1024M", "com.ubnt.airvision.Main", "start"]  
CMD ["/usr/sbin/unifi-video", "-D", "start"]  

