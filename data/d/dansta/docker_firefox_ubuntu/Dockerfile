# evaporating browser in the cloud  
# based on ubuntu, firefox and vnc  
FROM ubuntu:latest  
  
# Install vnc, xvfb in order to create a 'fake' display  
# Firefox and sudo because we dont want to run firefox as root  
RUN apt-get update && apt-get install -y x11vnc xvfb firefox sudo  
RUN groupadd firefoxgroup  
RUN useradd -m firefoxuser -G firefoxgroup -d /home/firefoxuser/  
RUN mkdir /root/.vnc  
# cache and settings for firefox  
RUN mkdir /home/firefoxuser/.mozilla  
RUN x11vnc -storepasswd 1234 /root/.vnc/passwd  
# autostart  
ADD firefox.sh /etc/X11/Xsession.d/30startupfirefox  
RUN chmod 755 /etc/X11/Xsession.d/30startupfirefox  
  
# document port  
EXPOSE 5900  
# switch -once into -forever if you want a persistent browser, add -proxy if
you need one  
CMD ["x11vnc", "-once", "-usepw", "-create", "-noipv6"]  

