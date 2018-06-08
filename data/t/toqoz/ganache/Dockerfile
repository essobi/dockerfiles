FROM debian:buster  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y \  
apt-transport-https \  
ca-certificates \  
curl \  
gnupg \  
\--no-install-recommends  
  
RUN apt-get update && apt-get -y install \  
git \  
g++ \  
libasound2 \  
libatk1.0-0 \  
libexpat1 \  
libgconf-2-4 \  
libgtk2.0-0 \  
libnss3 \  
libpango-1.0-0 \  
libx11-xcb1 \  
libxcomposite1 \  
libxcursor1 \  
libxdamage1 \  
libxext6 \  
libxfixes3 \  
libxi6 \  
libxrandr2 \  
libxrender1 \  
libxss1 \  
libxtst6 \  
make \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN git clone https://github.com/trufflesuite/ganache.git /ganache  
WORKDIR /ganache  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -y nodejs  
  
RUN npm install && npm run build-linux  
CMD dist/linux-unpacked/Ganache  

