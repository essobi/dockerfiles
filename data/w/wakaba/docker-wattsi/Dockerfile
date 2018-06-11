FROM wakaba/docker-wattsi:wattsi  
  
RUN apt-get update && \  
apt-get install -y grep perl python subversion unzip libxml-parser-perl && \  
rm -rf /var/lib/apt/lists/*  
  
RUN git clone https://github.com/whatwg/html-build  
  
WORKDIR /html-build  
RUN ./build.sh && \  
touch .cache/unicode.xml && \  
rm -fr ./output ./html  

