FROM ubuntu:14.04  
MAINTAINER Daniel Guerra  
RUN apt-get -yy update  
RUN apt-get -y install --no-install-recommends wget unzip firefox git ca-
certificates supervisor openbox xvfb x11vnc xterm  
WORKDIR /tmp  
RUN wget http://www.spot-
net.nl.vfcdn.net/downloads/spotlite/SpotLite\\(v2\\)Ubuntu.zip  
RUN unzip SpotLite\\(v2\\)Ubuntu.zip  
RUN dpkg --force-all -i spotlite-amd64.deb  
RUN rm -rf *  
RUN apt-get -yy -f install  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /home/spotlite  
RUN addgroup spotlite  
RUN useradd -m -g spotlite spotlite  
WORKDIR /opt  
RUN git clone \--recursive https://github.com/kanaka/noVNC.git  
RUN chown -R spotlite:spotlite noVNC  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD menu.xml /etc/xdg/openbox/menu.xml  
ADD spotlite /usr/bin/spotlite  
RUN chown spotlite:spotlite /usr/bin/spotlite*  
RUN chown -R spotlite:spotlite /home/spotlite  
WORKDIR /home/spotlite  
ENV DISPLAY :1  
ADD start /bin/start  
RUN update-alternatives --config x-www-browser  
EXPOSE 5900 6080  
CMD ["/bin/start"]  

