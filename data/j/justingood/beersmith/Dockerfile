FROM ubuntu:16.04  
RUN apt-get update && \  
apt-get install -y curl && \  
curl https://s3.amazonaws.com/beersmith2-3/BeerSmith-2.3.12_amd64.deb -o
/tmp/beersmith.deb && \  
apt-get install -y /tmp/beersmith.deb && \  
rm /tmp/beersmith.deb && \  
apt-get purge -y curl && \  
apt-get clean  
  
RUN mkdir -p /home/beersmith2/.beersmith2 && \  
chmod 777 -R /home/beersmith2  
  
ENV HOME /home/beersmith2  
  
CMD /usr/bin/beersmith2  

