FROM brujoand/dockzb  
  
MAINTAINER Anders Brujordet  
  
ENV SERVICE sickrage  
  
RUN installer apk python git && \  
installer -b apk python-dev gcc linux-headers openssl-dev musl-dev libffi-dev
&& \  
installer pip PyOpenSSL && \  
installer -c git "https://github.com/SickRage/SickRage"  
  
  
CMD [ "python", "/opt/SickRage/SickBeard.py", "--datadir", "/config", "--
nolaunch" ]  
  
EXPOSE 8081  

