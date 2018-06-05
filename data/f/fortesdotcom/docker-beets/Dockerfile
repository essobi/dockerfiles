FROM debian:stretch  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends python-pip python-setuptools mp3val
bs1770gain && \  
pip install -U wheel beautifulsoup4 beets flask pyacoustid pylast requests &&
\  
rm -rf /var/lib/apt/lists/*  
  
VOLUME /config /import /music  
  
ENV BEETSDIR /config  
  
WORKDIR /import  
  
COPY ./clean-and-import.sh /usr/bin/clean-and-import  

