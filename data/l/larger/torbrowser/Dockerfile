FROM debian:jessie  
  
RUN apt-get update && \  
apt-get install -y sudo wget xz-utils tightvncserver lxterminal fluxbox ca-
certificates \  
libasound2 libdbus-glib-1-2 libgtk2.0-0 libxrender1 libxt6  
  
RUN wget https://www.torproject.org/dist/torbrowser/6.5.1/tor-browser-
linux64-6.5.1_en-US.tar.xz \  
&& tar xvf tor-browser-linux64-6.5.1_en-US.tar.xz && rm -rf tor-browser-
linux64-6.5.1_en-US.tar.xz  
  
#user section  
ENV USER developer  
ENV HOME "/home/$USER"  
ENV VNC_PW Ssrmit09  
RUN useradd --create-home --home-dir $HOME \--shell /bin/bash $USER && \  
mkdir $HOME/.vnc/  
COPY vnc.sh $HOME/.vnc/  
COPY xstartup $HOME/.vnc/  
RUN chmod 760 $HOME/.vnc/vnc.sh $HOME/.vnc/xstartup && \  
chown -R $USER:$USER $HOME tor-browser_en-US  
  
USER "$USER"  
#Setup a VNC password  
RUN echo $VNC_PW | vncpasswd -f > ~/.vnc/passwd && \  
chmod 600 ~/.vnc/passwd  
  
EXPOSE 5901  
CMD ["/home/developer/.vnc/vnc.sh"]

