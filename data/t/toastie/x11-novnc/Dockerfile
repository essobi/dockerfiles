#  
# A dockerfile to run X11 through the browser with noVNC  
# Inspired by  
# https://github.com/codenvy/dockerfiles/tree/master/x11_vnc  
#  
# BUILD DOCKER: docker build -t toastie/x11-novnc .  
# RUN DOCKER: docker run -it -p 8080:8080 toastie/x11-novnc  
# TEST DOCKER: docker exec -it -p 8080:8080 toastie/x11-novnc /bin/bash  
FROM ubuntu  
MAINTAINER toastie <user@example.com>  
  
# Expose Port  
EXPOSE 8080  
  
# Set correct environment variables.  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL C.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV TZ Europe/Berlin  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
# Installing apps and clean up.  
RUN \  
apt-get update \  
&& apt-get -y upgrade \  
&& apt-get -y install \  
xvfb \  
x11vnc \  
supervisor \  
fluxbox \  
wget \  
ca-certificates \  
python \  
net-tools \  
&& apt-get clean  
  
  
# Download and install noVNC.  
RUN \  
mkdir -p /opt/noVNC/utils/websockify \  
&& wget -qO- "http://github.com/kanaka/noVNC/tarball/master" \  
| tar -zx \--strip-components=1 -C /opt/noVNC \  
&& wget -qO- "https://github.com/kanaka/websockify/tarball/master" \  
| tar -zx \--strip-components=1 -C /opt/noVNC/utils/websockify \  
&& ln -s /opt/noVNC/vnc.html /opt/noVNC/index.html  
  
  
# Configure & run supervisor  
COPY novnc.conf /etc/supervisor/conf.d/novnc.conf  
CMD ["/usr/bin/supervisord"]  

