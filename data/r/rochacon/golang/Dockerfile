from ubuntu:14.04  
maintainer Rodrigo Chacon <rochacon@gmail.com>  
run apt-get update -y  
run DEBIAN_FRONTEND=noninteractive apt-get install -y wget && apt-get clean  
run wget -qO- https://storage.googleapis.com/golang/go1.3.linux-amd64.tar.gz |
tar vxzC /usr/local  
env GOROOT /usr/local/go  
env PATH /usr/local/go/bin:$PATH  

