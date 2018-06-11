FROM ubuntu:16.04  
MAINTAINER whatsalinux  
RUN apt-get -yy update  
RUN apt-get -y install --no-install-recommends unzip sudo libfuse2 libx11-6
libx11-xcb1 libfontconfig1 supervisor xvfb x11vnc software-properties-common
openbox xterm  
RUN apt-get -y install --install-recommends openjdk-8-jdk-headless  
#RUN apt-get clean  
#RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN addgroup jbidwatcher  
RUN useradd -m -s /bin/bash -g jbidwatcher jbidwatcher  
RUN echo "jbidwatcher:jbidwatcher" | /usr/sbin/chpasswd  
RUN echo "jbidwatcher ALL=(ALL) ALL" >> /etc/sudoers  
RUN mkdir -p -m 0755 /opt/jbidwatcher  
ADD jbidwatcher.zip /opt/jbidwatcher/jbidwatcher.zip  
ADD start_jbidwatcher.sh /opt/jbidwatcher/start_jbidwatcher.sh  
WORKDIR /home/jbidwatcher  
RUN unzip -n -d /opt/jbidwatcher/ /opt/jbidwatcher/jbidwatcher.zip  
RUN chown jbidwatcher:jbidwatcher -R /opt/jbidwatcher/  
RUN chmod 755 -R /opt/jbidwatcher/*jbidwatcher.sh  
RUN ln -sf /opt/jbidwatcher/start_jbidwatcher.sh /usr/bin/jbidwatcher  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD menu.xml /etc/xdg/openbox/menu.xml  
RUN chown jbidwatcher:jbidwatcher -R /home/jbidwatcher  
ENV DISPLAY :1  
ADD start /bin/start  
USER jbidwatcher  
EXPOSE 5977  
CMD ["/bin/start"]  

