FROM jess/wine  
MAINTAINER Tibor Sári <tiborsari@gmx.de>  
  
RUN apt-get update && apt-get install -y \  
unzip \  
wget \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -m 777 /home/wine && \  
cd /home/wine && \  
wget http://www.heidisql.com/downloads/releases/HeidiSQL_9.3_Portable.zip && \  
unzip /home/wine/HeidiSQL_9.3_Portable.zip && \  
chmod -R 777 /home/wine  
  
CMD wine /home/wine/heidisql.exe

