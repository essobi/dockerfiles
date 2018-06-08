from ubuntu  
maintainer Gillis57<me@gill.is>  
  
RUN apt-get update  
  
RUN apt-get install -y libqt4-opengl python3-opengl python3-pyqt4
python3-pyqt4.qtopengl python3-numpy python3-scipy python3-pip git mtd-utils
gzip bzip2 tar arj lhasa p7zip p7zip-full cabextract cramfsprogs cramfsswap
squashfs-tools python wget zlib1g-dev liblzma-dev liblzo2-dev && \  
apt-get clean  
  
RUN pip3 install pyqtgraph  
  
RUN git clone https://github.com/devttys0/binwalk.git && \  
cd binwalk && \  
python setup.py install && \  
cd / && \  
rm -R binwalk/  
  
RUN wget http://www.capstone-engine.org/download/3.0.1/capstone-3.0.1.tgz && \  
tar -zxvf capstone-3.0.1.tgz && \  
cd capstone-3.0.1 && \  
./make.sh && \  
make install && \  
cd bindings/python && \  
python3 setup.py install && \  
cd / && \  
rm -R capstone-3.0.1.tgz && \  
rm -R capstone-3.0.1/  
  
RUN git clone https://github.com/devttys0/sasquatch && \  
cd sasquatch && \  
make && \  
sudo make install && \  
cd / && \  
rm -R sasquatch/  
  
RUN wget -O -
http://my.smithmicro.com/downloads/files/stuffit520.611linux-i386.tar.gz | tar
-zxv && \  
cp bin/unstuff /usr/local/bin/  
  
WORKDIR /opt  
  
ENTRYPOINT ["/usr/local/bin/binwalk"]  

