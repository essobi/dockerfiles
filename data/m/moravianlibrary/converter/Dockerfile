FROM ubuntu:trusty  
  
RUN apt-get update && apt-get install -y imagemagick build-essential && rm -rf
/var/lib/apt/lists/*  
RUN cpan Text::CSV_XS  
  
ADD libkdu_v77R.so /usr/lib/libkdu_v77R.so  
ADD kakadu/ /usr/local/bin  
Add scripts/ /scripts  

