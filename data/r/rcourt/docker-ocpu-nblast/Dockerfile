FROM opencpu/rstudio  
  
# ADD http://data.virtualflybrain.org/archive/site-library.tar.gz /site-
library.tar.gz  
# ADD http://data.virtualflybrain.org/archive/nblast.tar.gz /nblast.tar.gz  
VOLUME /data  
  
RUN chmod -R 777 /data  
  
RUN apt-get update && apt-get install -y wget git gzip tar less
libcurl4-openssl-dev libxml2-dev libX11-dev freeglut3 freeglut3-dev r-cran-rgl
libglu1-mesa-dev libgl1-mesa-dev xvfb libcairo2-dev libmagick++-dev
libpoppler-cpp-dev libwebp-dev  
  
COPY startNBLAST.sh /startNBLAST.sh  
  
COPY loadScript.R /loadScript.R  
  
RUN chmod +x /startNBLAST.sh  
  
COPY server.conf /etc/opencpu/server.conf  
  
COPY Rprofile /etc/opencpu/Rprofile  
  
CMD /startNBLAST.sh  

