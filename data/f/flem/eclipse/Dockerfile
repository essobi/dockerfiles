# DESCRIPTION: Run Eclipse IDE into a container  
# BUILD: docker build -t flem/eclipse .  
# RUN: mkdir $(pwd)/docker-eclipse  
# docker run -d --name eclipse \  
# -v /etc/localtime:/etc/localtime:ro \  
# -v /etc/timezone:/etc/timezone:ro \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \  
# -e DISPLAY=unix$DISPLAY \  
# -v $(pwd)/docker-eclipse:/home/developer \  
# flem/eclipse  
FROM openjdk:8-jdk  
MAINTAINER Franck Lemoine <franck.lemoine@flem.fr>  
  
# properly setup debian sources  
ENV DEBIAN_FRONTEND=noninteractive  
  
USER root  
  
RUN set -x \  
&& wget -q -O /tmp/eclipse.tar.gz
http://download.eclipse.org/technology/epp/downloads/release/neon/2/eclipse-
java-neon-2-linux-gtk-x86_64.tar.gz \  
&& tar -xf /tmp/eclipse.tar.gz -C /opt \  
&& rm /tmp/eclipse.tar.gz  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends libxext-dev libxrender-dev
libxtst-dev libgtk2.0-0 libcanberra-gtk-module sudo \  
&& apt-get clean autoclean \  
&& rm -r /var/lib/apt/lists/* \  
&& rm -rf /tmp/*  
  
ADD eclipse.sh /usr/local/bin/eclipse.sh  
  
RUN chmod +x /usr/local/bin/eclipse.sh \  
&& mkdir -p /home/developer \  
&& echo "developer:x:1000:1000:Developer,,,:/home/developer:/bin/bash" >>
/etc/passwd \  
&& echo "developer:x:1000:" >> /etc/group \  
&& echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer \  
&& chmod 0440 /etc/sudoers.d/developer \  
&& chown developer:developer -R /home/developer \  
&& chown root:root /usr/bin/sudo && chmod 4755 /usr/bin/sudo  
  
USER developer  
ENV HOME /home/developer  
WORKDIR /home/developer  
  
ENTRYPOINT ["/usr/local/bin/eclipse.sh"]  

