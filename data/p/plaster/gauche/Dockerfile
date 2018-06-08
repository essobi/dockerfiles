FROM debian:jessie  
RUN apt update \  
&& apt upgrade -y \  
&& apt install -y wget build-essential \  
&& wget -O Gauche-0.9.5.tgz \--no-verbose
'http://downloads.sourceforge.net/project/gauche/Gauche/Gauche-0.9.5.tgz?r=&ts=1479315272&use_mirror=jaist'
\  
&& tar xzf Gauche-0.9.5.tgz \  
&& cd Gauche-0.9.5 \  
&& ./configure \  
&& make \  
&& make install  

