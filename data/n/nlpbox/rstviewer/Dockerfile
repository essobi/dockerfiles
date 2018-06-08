FROM nlpbox/nlpbox-base:16.04  
RUN apt-get update -y && apt-get upgrade -y && \  
apt-get install -y python-pip firefox && \  
pip2 install selenium==3.9.0 \  
pudb pytest==3.5.1 pillow==5.1.0 imagehash==4.0  
  
# settings for interactive debugging  
ADD pudb.cfg /root/  
  
# install geckodriver for headless browsing with selenium  
WORKDIR /usr/local/bin  
RUN wget
https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz
&& \  
tar -xvzf geckodriver-v0.19.1-linux64.tar.gz && \  
rm geckodriver-v0.19.1-linux64.tar.gz  
  
WORKDIR /opt  
RUN git clone https://github.com/arne-cl/rstviewer  
  
WORKDIR /opt/rstviewer  
RUN python2 setup.py install && pip2 install  
  
ENTRYPOINT ["rstviewer"]  

