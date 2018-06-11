FROM mono:4.4.0.182  
RUN echo "deb http://httpredir.debian.org/debian jessie main" >
/etc/apt/sources.list  
RUN echo "deb-src http://httpredir.debian.org/debian jessie main" >>
/etc/apt/sources.list  
  
RUN echo "deb http://httpredir.debian.org/debian jessie-updates main" >>
/etc/apt/sources.list  
RUN echo "deb-src http://httpredir.debian.org/debian jessie-updates main" >>
/etc/apt/sources.list  
  
RUN echo "deb http://security.debian.org/ jessie/updates main" >>
/etc/apt/sources.list  
RUN echo "deb-src http://security.debian.org/ jessie/updates main" >>
/etc/apt/sources.list  
  
RUN apt-get -y update && apt-get install -y libc6 && rm -rf
/var/lib/apt/lists/*  
  

