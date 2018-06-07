FROM nvidia/cuda:8.0-runtime  
  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \  
python-pip python-qt4 pyqt4-dev-tools \  
python-opencv python-numpy python-scipy python-matplotlib \  
curl x11vnc xvfb net-tools \  
&& rm -rf /var/lib/apt/lists/*  
RUN pip install chainer==1.24.0  
  
RUN mkdir -p /opt/noVNC/utils/websockify \  
&& curl -SL https://github.com/novnc/noVNC/archive/7e19216.tar.gz | tar zx
--strip-components=1 -C /opt/noVNC \  
&& curl -SL https://github.com/kanaka/websockify/archive/5b7f722.tar.gz | tar
zx --strip-components=1 -C /opt/noVNC/utils/websockify  
  
RUN mkdir -p /opt/GUINNESS && curl -SL
https://github.com/HirokiNakahara/GUINNESS/archive/007488e.tar.gz | tar zx
--strip-components=1 -C /opt/GUINNESS  
  
COPY run.sh /root/run.sh  
COPY index.html /opt/noVNC/  
  
EXPOSE 6080  
CMD /root/run.sh  

