FROM docker:18  
  
MAINTAINER Lucas POUZAC <lucas.pouzac.pro@gmail.com>  
  
ARG VERSION_PACKER="1.2.0"  
  
RUN wget -O packer.zip
https://releases.hashicorp.com/packer/${VERSION_PACKER}/packer_${VERSION_PACKER}_linux_amd64.zip
\  
&& unzip packer.zip -d /bin \  
&& rm packer.zip  

