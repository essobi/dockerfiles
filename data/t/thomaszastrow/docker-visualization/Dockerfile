FROM ubuntu:latest  
ENV DISPLAY=:0.0  
RUN apt-get update  
RUN apt-get install -y x11vnc fluxbox git xterm xvfb socat netstat-nat python  
  
RUN apt-get install -y libglu1-mesa  
  
RUN ln -s /usr/bin/netstat-nat /usr/bin/netstat  
  
RUN git clone https://github.com/kanaka/noVNC.git /opt/novnc  
RUN git clone https://github.com/kanaka/websockify /opt/novnc/utils/websockify  
RUN sed -i -- "s/ps -p/ps -o pid | grep/g" /opt/novnc/utils/launch.sh  
  
COPY startscript.sh /usr/local/bin/startscript.sh  
  
EXPOSE 6080  
ENTRYPOINT ["/usr/local/bin/startscript.sh"]  

