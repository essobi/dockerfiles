FROM phusion/baseimage:0.9.22  
# Set correct environment variables  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL C.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
#ENV TZ=US/Pacific  
ENV SCREEN_RESOLUTION 1280x900  
#RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ >
/etc/timezone  
# install skypeforlinux  
RUN apt-get update && \  
curl https://repo.skype.com/data/SKYPE-GPG-KEY | apt-key add - && \  
echo "deb [arch=amd64] https://repo.skype.com/deb stable main" | \  
tee /etc/apt/sources.list.d/skypeforlinux.list && \  
apt-get update && \  
apt-get install -y skypeforlinux=8.15.0.4 \  
xvfb \  
x11vnc \  
supervisor \  
fluxbox \  
git-core \  
git \  
apt-transport-https  
  
# House cleaning  
RUN apt-get autoclean  
  
# Obtain noVNC  
WORKDIR /root  
RUN git clone https://github.com/novnc/noVNC.git && ln -s
/root/noVNC/vnc_auto.html /root/noVNC/index.html  
  
# Docker's supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Set display  
ENV DISPLAY :0  
# Expose Port (Note: if you change it do it as well in surpervisord.conf)  
EXPOSE 5900  
EXPOSE 8083  
CMD ["/usr/bin/supervisord"]  

