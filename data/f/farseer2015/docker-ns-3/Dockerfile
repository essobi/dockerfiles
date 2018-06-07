FROM ubuntu:14.04  
ADD sources.list /etc/apt/sources.list  
  
RUN apt-get update && apt-get install -y python-dev python-pygraphviz python-
kiwi \  
python-pygoocanvas python-gnome2 python-rsvg ipython  
  
RUN apt-get install -y wget tar g++  
  
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
  
RUN wget https://www.nsnam.org/release/ns-allinone-3.22.tar.bz2 -O
/home/developer/ns-3.tar.bz2  
RUN cd /home/developer && tar jxf ns-3.tar.bz2 && cd ns-allinone-3.22 && \  
./build.py --enable-examples --enable-tests --build-options=--progress  
RUN rm /home/developer/ns-3.tar.bz2 && sudo apt-get autoclean && sudo apt-get
clean  

