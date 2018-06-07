FROM ubuntu:14.04  
# ADD sources.list /etc/apt/sources.list  
RUN apt-get update && apt-get install -y python-dev python-pygraphviz python-
kiwi \  
python-pygoocanvas python-gnome2 python-rsvg  
  
RUN apt-get install -y wget tar g++ git  
RUN apt-get install -y build-essential libsqlite3-dev libcrypto++-dev
libboost-all-dev pkg-config  
  
# Replace 1000 with your user / group id  
RUN export uid=1000 gid=1000 && \  
mkdir -p /home/developer && \  
echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >>
/etc/passwd && \  
echo "developer:x:${uid}:" >> /etc/group && \  
echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \  
chmod 0440 /etc/sudoers.d/developer && \  
chown ${uid}:${gid} -R /home/developer  
  
USER developer  
ENV HOME /home/developer  
  
RUN cd /home/developer && \  
git clone https://github.com/named-data/ndn-cxx.git ndn-cxx && \  
git clone https://github.com/cawka/ns-3-dev-ndnSIM.git ns-3 && \  
git clone https://github.com/cawka/pybindgen.git pybindgen && \  
git clone https://github.com/named-data/ndnSIM.git ns-3/src/ndnSIM  
  
RUN cd /home/developer/ndn-cxx && ./waf configure && ./waf && sudo ./waf
install  
RUN cd /home/developer/ns-3 && ./waf configure --enable-examples && ./waf  

