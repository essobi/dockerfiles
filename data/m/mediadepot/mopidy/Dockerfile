FROM mediadepot/base:debian  
  
#Create mopidy folder structure & set as volumes  
RUN mkdir -p /srv/mopidy/app && \  
mkdir -p /srv/mopidy/config && \  
mkdir -p /srv/mopidy/data  
  
WORKDIR /srv/mopidy/app  
  
RUN apt-get update && apt-get install -y \  
wget python-pip cron && \  
wget -q -O - https://apt.mopidy.com/mopidy.gpg | apt-key add - && \  
wget -q -O /etc/apt/sources.list.d/mopidy.list
https://apt.mopidy.com/jessie.list && \  
  
apt-get update && apt-get install -y \  
mopidy && \  
  
pip install \  
pafy \  
Mopidy-GMusic \  
Mopidy-Mopify \  
Mopidy-Iris \  
Mopidy-Moped \  
Mopidy-Local-SQLite \  
Mopidy-SoundCloud \  
Mopidy-Party && \  
  
rm -rf /var/lib/apt/lists/*  
  
#copy over the default configuraiton & service run/finish commands  
COPY rootfs /  
  
VOLUME ["/srv/mopidy/config", "/srv/mopidy/data"]  
EXPOSE 8081 6600  
ENTRYPOINT ["/init"]  

