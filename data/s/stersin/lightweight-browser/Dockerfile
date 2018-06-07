FROM ubuntu  
  
RUN apt-get update && apt-get install -y python python-webkit python-dbus
libcanberra-gtk-module dbus-x11  
  
ADD browser.py /usr/local/bin/browser.py  
  
ENTRYPOINT ["browser.py"]  

