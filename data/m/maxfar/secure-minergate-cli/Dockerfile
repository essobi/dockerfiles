FROM ubuntu:14.04  
RUN apt-get update \  
&& apt-get -qq --no-install-recommends install \  
ca-certificates \  
wget \  
&& rm -r /var/lib/apt/lists/*  
  
RUN wget -q --content-disposition https://minergate.com/download/deb-cli \  
&& dpkg -i *.deb \  
&& rm *.deb  
  
RUN useradd -m massimo.farinelli.roma@gmail.com  
USER massimo.farinelli.roma@gmail.com  
  
CMD minergate-cli -user massimo.farinelli.roma@gmail.com -fcn+xmr

