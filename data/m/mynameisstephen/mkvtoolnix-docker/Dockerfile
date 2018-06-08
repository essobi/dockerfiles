FROM ubuntu:latest  
  
RUN apt-get update  
RUN apt-get install -y wget software-properties-common python-software-
properties  
RUN wget -q -O - https://www.bunkus.org/gpg-pub-moritzbunkus.txt | sudo apt-
key add -  
RUN add-apt-repository -y "deb http://www.bunkus.org/ubuntu/trusty/ ./"  
RUN apt-get update  
RUN apt-get -qy install mkvtoolnix && apt-get clean  
CMD ["echo", "mkvinfo|mkvinfo-text|mkvmerge|mkvpropedit|mkvextract"]

