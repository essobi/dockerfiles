FROM ubuntu:18.04  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
dcmtk \  
orthanc \  
orthanc-dicomweb \  
&& rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["Orthanc"]  

