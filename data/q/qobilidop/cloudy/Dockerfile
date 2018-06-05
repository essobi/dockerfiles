# http://www.nublado.org/wiki/NewC13  
FROM ubuntu  
  
RUN apt-get update && apt-get install -y \  
curl \  
g++ \  
make  
  
# Download  
# http://www.nublado.org/wiki/DownloadLinks  
WORKDIR $HOME/cloudy  
RUN curl -O http://data.nublado.org/cloudy_releases/c13/c13.05.tar.gz  
RUN tar xvfz c13.05.tar.gz  
ENV CLOUDYPATH $HOME/cloudy/c13.05  
# Compile  
# http://www.nublado.org/wiki/CompilingCloudyC13  
WORKDIR $CLOUDYPATH/source  
RUN make  
  
# Export executables  
# http://www.nublado.org/wiki/RunningC13  
RUN mkdir $CLOUDYPATH/bin  
WORKDIR $CLOUDYPATH/bin  
RUN ln -s $CLOUDYPATH/source/cloudy.exe cloudy.exe  
RUN echo "cloudy.exe -r \$1" > run  
RUN chmod +x run  
ENV PATH $CLOUDYPATH/bin:$PATH  
  
WORKDIR /data  
VOLUME ["/data"]  

