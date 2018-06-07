FROM selenium/node-base  
  
RUN sudo apt-get update && sudo apt-get install -y software-properties-common  
RUN /bin/bash && sudo dpkg --add-architecture i386 && sudo add-apt-repository
ppa:wine/wine-builds && sudo apt-get update && sudo apt-get install -y
--install-recommends winehq-staging  
  
ADD IEDriverServer.exe /home/seluser  
ADD IE8-WindowsXP-x86-ENU.exe /home/seluser  
ADD jre-8u5-windows-i586.exe /home/seluser  
ADD wine_profile.tar.gz /home/seluser  
ADD entry_point.sh /opt/bin/  
ADD config.json /opt/selenium/config.json  
#RUN WINEPREFIX="$HOME/.wine/" WINEARCH=win32 wine wineboot  
#RUN cd /home/seluser && xvfb-run wine IE8-WindowsXP-x86-ENU.exe /quiet
/update-no /forcerestart  
  
USER seluser  
EXPOSE 5555  
  

