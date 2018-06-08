FROM ubuntu:latest  
  
RUN apt-get -y update && apt-get install -y wget zip \  
&& mkdir instancescompet2017maintrack \  
&& wget https://baldur.iti.kit.edu/sat-competition-2017/benchmarks/Main.zip \  
&& unzip Main.zip -d instancescompet2017maintrack \  
&& rm -rf Main.zip  

