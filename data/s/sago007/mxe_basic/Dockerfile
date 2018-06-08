FROM debian:8  
#Use http://pkg.mxe.cc/  
#First add the repository and install the static gcc compiler. This ensures
that everything basic is setup.  
RUN echo "deb http://pkg.mxe.cc/repos/apt/debian wheezy main" > \  
/etc/apt/sources.list.d/mxeapt.list && \  
apt-key adv --keyserver keyserver.ubuntu.com \--recv-keys
D43A795B73B16ABE9643FE1AFD8FFF16DB45C6AB && \  
apt-get update && \  
apt-get install -y mxe-i686-w64-mingw32.static-gcc \  
nsis \  
zip \  
libtool  
#All packages!  
#RUN apt-get update && wget -O -
http://pkg.mxe.cc/repos/apt/debian/dists/jessie/main/binary-amd64/Packages |
grep Package | awk '{print $2}' | xargs apt-get install -y  
#Set the path  
env PATH
/usr/lib/mxe/usr/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  

