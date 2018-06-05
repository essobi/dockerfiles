FROM ubuntu:17.10 as package  
WORKDIR /bibutils  
RUN apt update \  
&& apt install -y build-essential wget \  
&& wget --output-document bibutils.tgz
https://sourceforge.net/projects/bibutils/files/latest/download?source=files \  
&& tar -xvzf bibutils.tgz \  
&& rm bibutils.tgz \  
&& cd /bibutils*/* \  
&& ./configure \  
&& make deb && mv update/*.deb /bibutils.deb  
  
FROM ubuntu:17.10  
COPY \--from=package /bibutils.deb .  
RUN dpkg -i --force-architecture bibutils.deb \  
&& rm bibutils.deb  
CMD ['/bin/bash']  

