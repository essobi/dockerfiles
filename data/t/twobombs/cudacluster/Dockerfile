FROM twobombs/deploy-nvidia-docker  
  
RUN apt-get update&&apt-get install -y git software-properties-common ant
openjdk-8-jdk qv4l2 python-software-properties python-setuptools
python3-setuptools python-migrate && apt-get clean all  
  
RUN git clone \--recursive https://github.com/stevenrobertson/cuburn.git  
RUN git clone \--recursive https://github.com/mebigfatguy/apophysis-j.git  
  
RUN cd /apophysis-j && ant  
  
RUN add-apt-repository universe && apt-get update && apt-get -y --force-yes
upgrade && export DEBIAN_FRONTEND=noninteractive && apt-get install -y
libboost-all-dev python-pip phoronix-test-suite && apt-get clean all  
  
RUN add-apt-repository ppa:paulo-miguel-dias/mesa -y && apt-get update && apt
-y dist-upgrade && apt-get clean all  
  
RUN pip install numpy scipy  
  
EXPOSE 6080  
ENTRYPOINT /root/run  

