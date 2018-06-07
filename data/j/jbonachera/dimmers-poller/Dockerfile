FROM pritunl/archlinux  
MAINTAINER Julien BONACHERA <julien@bonachera.fr>  
  
COPY . /usr/share/dimmers-poller  
RUN pacman -S --noconfirm python3 python-pip && \  
useradd -r dimmers-poller && \  
cd /usr/share/dimmers-poller && \  
pip install -r requirements.txt  
USER dimmers-poller  
CMD /usr/share/dimmers-poller/server.py  

