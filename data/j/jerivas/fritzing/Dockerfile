FROM dockerfile/ubuntu  
RUN \  
apt-get update && \  
apt-get install -y aptitude fritzing && \  
rm -rf /var/lib/apt/lists/*  
  
# Create a user  
RUN adduser fritzing  
USER fritzing  
ENV HOME /home/fritzing  
CMD []  
  
WORKDIR /home/fritzing  
RUN wget
http://fritzing.org/download/0.9.1b/linux-64bit/fritzing-0.9.1b.linux.AMD64.tar.bz2
-O /home/fritzing/fritzing-0.9.1b.linux.AMD64.tar.bz2 && \  
tar xjv -f /home/fritzing/fritzing-0.9.1b.linux.AMD64.tar.bz2 -C
/home/fritzing && \  
mkdir /home/fritzing/docs && \  
wget https://github.com/adafruit/Fritzing-Library/raw/master/AdaFruit.fzbz -O
/home/fritzing/AdaFruit.fzbz  
  
VOLUME /home/fritzing/docs  
WORKDIR /home/fritzing/docs  
  
ENTRYPOINT ["/home/fritzing/fritzing-0.9.1b.linux.AMD64/Fritzing", ""]  
  

