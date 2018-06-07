from ubuntu  
  
env SYNCTHING_VERSION=v0.14.47  
  
run apt-get update && \  
apt-get install -y wget ca-certificates && \  
wget --quiet
https://github.com/syncthing/syncthing/releases/download/$SYNCTHING_VERSION/syncthing-
linux-amd64-$SYNCTHING_VERSION.tar.gz -O- | tar xfz - -C /opt && \  
ln -s /opt/syncthing-linux-amd64-$SYNCTHING_VERSION/syncthing /usr/local/bin
&& \  
rm -rf /var/lib/apt/lists/*  

