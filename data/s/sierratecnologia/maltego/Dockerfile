# Base docker image  
FROM sierratecnologia/java:7  
MAINTAINER Ricardo Rebello Sierra <contato@ricardosierra.com.br>  
  
# Install dependencies  
RUN apt-get update && apt-get install -y \  
libasound2 \  
libgconf-2-4 \  
libgnome-keyring-dev \  
libgtk2.0-0 \  
libnotify4 \  
libnss3 \  
libxtst6 \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV MALTEGO_VERSION 4.0.11.9358  
RUN wget -c
http://www.paterva.com/malv4/community/MaltegoCE.v${MALTEGO_VERSION}.deb \  
&& dpkg -i MaltegoCE.v${MALTEGO_VERSION}.deb  
  
# Autorun maltego  
WORKDIR /var/www  
CMD maltego  

