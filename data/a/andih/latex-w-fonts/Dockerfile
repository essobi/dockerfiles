FROM ubuntu:latest  
MAINTAINER Andreas Herten <a.herten@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -q && \  
apt-get install -qy texlive-full python-pygments git wget biber && \  
apt-get clean  
  
RUN git clone \--depth 1 https://github.com/google/fonts.git google-fonts  
RUN mkdir -p /usr/share/fonts/truetype/google-fonts/  
RUN find $PWD/google-fonts/ -name "*.ttf" -exec install -m644 {}
/usr/share/fonts/truetype/google-fonts/ \; || return 1  
RUN rm -rf $PWD/google-fonts  
  
RUN git clone \--depth 1 -b release https://github.com/adobe-fonts/source-
sans-pro.git adobe-fonts-source-sans-pro  
RUN git clone \--depth 1 -b release https://github.com/adobe-fonts/source-
serif-pro.git adobe-fonts-source-serif-pro  
RUN git clone \--depth 1 -b release https://github.com/adobe-fonts/source-
code-pro.git adobe-fonts-source-code-pro  
RUN mkdir -p /usr/share/fonts/opentype/adobe-fonts/  
RUN find $PWD/adobe* -name "*.otf" -exec install -m644 {}
/usr/share/fonts/opentype/adobe-fonts/ \; || return 1  
RUN rm -rf $PWD/adobe*  
  
RUN fc-cache -f -v  
  
WORKDIR /data  
VOLUME /data  

