#  
# A dockerfile to run X11 through the browser with noVNC  
# Inspired by  
# https://github.com/codenvy/dockerfiles/tree/master/x11_vnc  
#  
# BUILD DOCKER: docker build -t toastie/x11-novnc .  
# RUN DOCKER: docker run -it -p 8080:8080 toastie/x11-novnc  
# TEST DOCKER: docker exec -it -p 8080:8080 toastie/x11-novnc /bin/bash  
  
FROM ubuntu  
  
# Expose Port  
EXPOSE 8080  
  
# Set correct environment variables.  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANG ja_JP.UTF-8  
ENV LC_ALL ${LANG}  
ENV LANGUAGE ${LANG}  
ENV TZ Asia/Tokyo  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
# Installing apps and clean up.  
RUN \  
apt-get update \  
&& apt-get -y install \  
xvfb \  
x11vnc \  
supervisor \  
wget \  
ca-certificates \  
python \  
net-tools \  
&& apt-get clean  
  
# Download and install noVNC.  
RUN \  
mkdir -p /opt/noVNC/utils/websockify \  
&& wget -qO- "http://github.com/kanaka/noVNC/tarball/master" \  
| tar -zx --strip-components=1 -C /opt/noVNC \  
&& wget -qO- "https://github.com/kanaka/websockify/tarball/master" \  
| tar -zx --strip-components=1 -C /opt/noVNC/utils/websockify \  
&& ln -s /opt/noVNC/vnc.html /opt/noVNC/index.html  
  
# Install some additins.  
RUN \  
apt-get update \  
&& apt-get -y install \  
fluxbox \  
chromium-browser \  
fonts-takao-gothic \  
mozc-server \  
&& apt-get clean  
  
# Configure & run supervisor  
COPY novnc.conf /etc/supervisor/conf.d/novnc.conf  
CMD ["/usr/bin/supervisord"]  

