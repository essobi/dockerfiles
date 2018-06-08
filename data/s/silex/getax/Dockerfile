from openjdk:8  
run apt update && apt install -y curl evince libwebkitgtk-1.0-0  
  
arg GETAX_URL=http://www.getax.ch/getaxpp/2016/getax2016-v110.tar.gz  
  
run curl $GETAX_URL | \  
tar -C /srv -xz && \  
mv /srv/getax-pp* /srv/getax && \  
ln -s /srv/getax/getax-pp* /srv/getax/getax  
  
cmd ["/srv/getax/getax"]  

