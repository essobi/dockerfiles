FROM bioconductor/devel_base2  
  
USER root  
RUN apt update && apt install -y openjdk-8-jdk libpcre3-dev liblzma-dev
libbz2-dev && \  
apt full-upgrade && apt autoremove && apt autoclean && \  
ln -s /usr/lib/jvm/java-8-openjdk-amd64/jre/lib/amd64/server/libjvm.so
/usr/lib/libjvm.so  
  
USER rstudio  
RUN R -e 'source("https://bioconductor.org/biocLite.R")' && R -e
'BiocInstaller::biocLite("BridgeDbR")'  

