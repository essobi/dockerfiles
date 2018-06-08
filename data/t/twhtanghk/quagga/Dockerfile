FROM debian  
  
RUN apt-get update \  
&& apt-get install -y quagga procps \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir /run/quagga \  
&& chown quagga.quagga /run/quagga  
  
ADD data/zebra.conf /etc/quagga/  
ADD data/ripd.conf /etc/quagga/  
  
CMD zebra  

