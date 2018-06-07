FROM digitallyseamless/nodejs-bower-grunt:5  
MAINTAINER kingjan1999 <king-jan1999@hotmail.de>  
  
RUN echo "deb http://http.us.debian.org/debian jessie main contrib non-free"
>> /etc/apt/sources.list  
RUN echo "deb http://security.debian.org jessie/updates main contrib non-free"
>> /etc/apt/sources.list  
RUN apt-get update && apt-get install -y texlive-full biber ttf-mscorefonts-
installer pdftk  

