FROM node:9  
# Install yarn + gulp  
RUN npm install -g gulp  
  
# Install git (needed for bower)  
RUN apt-get update && \  
apt-get install -y --no-install-recommends git && \  
apt-get clean && \  
rm -r /var/lib/apt/lists/*  
# Requirements for headless chrome  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
gconf-service libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3
libexpat1 libfontconfig1 libgcc1 \  
libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4
libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 \  
libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6
libxfixes3 libxi6 libxrandr2 \  
libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1
libnss3 lsb-release xdg-utils wget && \  
apt-get clean && \  
rm -r /var/lib/apt/lists/*  
# Tools to change the uid on run  
RUN apt-get update && \  
apt-get install -y --no-install-recommends sudo && \  
apt-get clean && \  
rm -r /var/lib/apt/lists/*  
  
COPY entrypoint-chuid /usr/local/bin  
ENTRYPOINT ["entrypoint-chuid"]  
  

