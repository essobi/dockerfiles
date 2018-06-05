FROM ubuntu  
  
RUN apt-get update \  
&& apt-get install -y gcc make wget \  
&& apt-get clean -y  
  
WORKDIR /usr/local  
RUN mkdir ahf \  
&& wget -qO- http://popia.ft.uam.es/AHF/files/ahf-v1.0-091.tgz \  
| tar -C ahf --strip-components 1 -xz  
  
WORKDIR /usr/local/ahf  
RUN make AHF MergerTree \  
&& mv bin/AHF-v1.0-091 bin/AHF \  
&& ln -s $PWD/bin/AHF /usr/local/bin/ \  
&& ln -s $PWD/bin/MergerTree /usr/local/bin/ \  
&& make clean  
  
WORKDIR /data  
VOLUME ["/data"]  

