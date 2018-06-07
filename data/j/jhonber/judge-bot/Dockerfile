FROM debian:testing  
  
RUN echo "deb http://ftp.de.debian.org/debian testing contrib" >>
/etc/apt/sources.list \  
&& echo "deb http://ftp.de.debian.org/debian testing non-free" >>
/etc/apt/sources.list \  
&& echo "deb http://ftp.de.debian.org/debian testing main" >>
/etc/apt/sources.list  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
openjdk-8-jdk \  
openjdk-8-jre \  
python \  
time \  
vim \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  

