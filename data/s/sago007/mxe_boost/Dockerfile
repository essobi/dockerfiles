FROM sago007/mxe_basic  
#All packages!  
RUN apt-get update && wget -O -
http://pkg.mxe.cc/repos/apt/debian/dists/jessie/main/binary-amd64/Packages |
grep Package | grep boost | awk '{print $2}' | xargs apt-get install -y  
  

