FROM kalilinux/kali-linux-docker  
  
RUN apt-get update && apt-get install -y \  
fierce \  
nmap \  
theharvester \  
nikto \  
whatweb \  
wpscan \  
joomscan \  
python \  
python-pip \  
python3-pip \  
sqlmap \  
git \  
expect \  
python-dnspython \  
&& apt-get clean \  
&& pip install pypwned termcolor \  
&& pip3 install python-libnmap termcolor  
  
# AutoPoke  
RUN git clone https://github.com/ValtteriL/AutoPoke.git && \  
echo 'export PATH=$PATH:/AutoPoke' >> ~/.bashrc && \  
echo 'export PATH=$PATH:/AutoPoke/scripts' >> ~/.bashrc  
  
# Install stuff from github  
# Sublist3r  
RUN cd /opt && \  
git clone https://github.com/aboul3la/Sublist3r.git && \  
cd Sublist3r && \  
pip install -r requirements.txt && \  
chmod +x sublist3r.py && \  
echo 'export PATH=$PATH:/opt/Sublist3r' >> ~/.bashrc && \  
cd /  
  
# python nmap library  
RUN cd /opt && \  
git clone https://github.com/savon-noir/python-libnmap.git && \  
cd python-libnmap && \  
python setup.py install && \  
cd /  
  
# SubBrute  
RUN cd /opt && \  
git clone https://github.com/TheRook/subbrute.git && \  
echo 'export PATH=$PATH:/opt/subbrute' >> ~/.bashrc && \  
cd /  
  
# add volume  
VOLUME /loot  
  
# add newly installed packages to path  
ENV PATH /opt/Sublist3r:$PATH  
ENV PATH /opt/subbrute:$PATH  
ENV PATH /AutoPoke:$PATH  
ENV PATH /AutoPoke/scripts:$PATH  
  
# entrypoint to autopoke, default argument to show information  
ENTRYPOINT ["/AutoPoke/autopoke"]  
CMD ["--help"]  

