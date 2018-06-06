FROM alpine  
  
MAINTAINER Nay San nay.san@anu.edu.au  
  
ENV PRAAT_VER 6028  
  
RUN wget
http://www.fon.hum.uva.nl/praat/praat${PRAAT_VER}_linux64barren.tar.gz \  
&& tar xzf praat${PRAAT_VER}_linux64barren.tar.gz -C /usr/bin \  
&& rm praat${PRAAT_VER}_linux64barren.tar.gz  

