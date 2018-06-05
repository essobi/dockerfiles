from ubuntu  
  
run apt-get update  
run apt-get install -y -q wget curl  
run apt-get install -y -q build-essential  
run apt-get install -y -q cmake  
run apt-get install -y -q python2.7 python2.7-dev  
run wget
'https://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11-py2.7.egg'
&& /bin/sh setuptools-0.6c11-py2.7.egg && rm -f setuptools-0.6c11-py2.7.egg  
run curl https://bootstrap.pypa.io/get-pip.py | python2.7  
run pip install numpy  
run apt-get install -y -q libavformat-dev libavcodec-dev libavfilter-dev
libswscale-dev  
run apt-get install -y -q libjpeg-dev libpng-dev libtiff-dev libjasper-dev
zlib1g-dev libopenexr-dev libxine-dev libeigen3-dev libtbb-dev  
run apt-get install -y -q unzip  
add build_opencv.sh /build_opencv.sh  
run /bin/sh /build_opencv.sh  
run apt-get install -y -q python-scipy  
run rm -rf /build_opencv.sh  

