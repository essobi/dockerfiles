from ubuntu:12.10  
maintainer Chilijung "http://github.com/chilijung"  
run apt-get update  
run apt-get install -y -q wget curl  
run apt-get install -y -q g++  
run apt-get install -y -q python  
run apt-get install -y -q libusb-1.0-0-dev  
run apt-get install -y -q freeglut3-dev  
  
  
run wget "https://github.com/OpenNI/OpenNI/archive/Stable-1.5.7.10.tar.gz"  
run tar -xvf Stable-1.5.7.10.tar.gz  
  
run apt-get install -y openjdk-6-jdk  
run apt-get install -y doxygen  
run apt-get install -y graphviz  
  
run apt-get install -y make  
run cd ./OpenNI-Stable-1.5.7.10/Platform/Linux/CreateRedist && ./RedistMaker  
run cd ./OpenNI-Stable-1.5.7.10/Platform/Linux/Redist/OpenNI-Bin-Dev-
Linux-x64-v1.5.7.10 && sudo ./install.sh  

