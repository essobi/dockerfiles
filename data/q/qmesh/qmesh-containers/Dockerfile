#Base container with Ubuntu 16.04 (Xenial Long Term Release), qgis ltr (latest
Long Term Release) and gmsh 3.0.4  
#Build with: docker build -t ubuntu1604_qgisltr_gmsh304 -f
ubuntu1604_qgisltr_gmsh304 .  
#Run with : docker run -it -v /tmp/.X11-unix:/tmp/.X11-unix -e
DISPLAY=unix$DISPLAY ubuntu1604_qgisltr_gmsh304  
FROM ubuntu:16.04  
#Add qgis package servers  
RUN echo "deb http://qgis.org/debian-ltr xenial main" >> /etc/apt/sources.list
&& \  
echo "deb-src http://qgis.org/debian-ltr xenial main" >> /etc/apt/sources.list
&& \  
apt-key adv --keyserver keyserver.ubuntu.com \--recv-key CAEB3DC3BDF7FB45 && \  
apt-get update && \  
#Install qgis  
apt-get install -y qgis python-qgis qgis-plugin-grass && \  
#Install a few other dependencies  
apt-get install -y --no-install-recommends git python-setuptools && \  
apt-get install -y --no-install-recommends wget make g++ && \  
apt-get install -y python-scipy python-scipy-dbg python-pip && \  
pip install --upgrade pip && \  
#Install gmsh  
wget http://gmsh.info/bin/Linux/gmsh-3.0.4-Linux64.tgz && \  
tar -xzf gmsh-3.0.4-Linux64.tgz && \  
cd gmsh-3.0.4-Linux && \  
cp -r bin/* /usr/local/bin/ && \  
cd ../ && \  
rm -rf gmsh-3.0.4-Linux64.tgz gmsh-3.0.4-Linux && \  
#Clean up, to reduce image size  
rm -rf /var/lib/apt/lists/*  

