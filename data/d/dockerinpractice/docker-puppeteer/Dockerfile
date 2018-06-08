FROM ubuntu:16.04  
# Install dependencies  
RUN apt-get update -y && apt-get install -y npm python-software-properties
curl git libpangocairo-1.0-0 libx11-xcb1 libxcomposite1 libxcursor1
libxdamage1 libxi6 libxtst6 libnss3 libcups2 libxss1 libxrandr2 libgconf-2-4
libasound2 libatk1.0-0 libgtk-3-0 vim gconf-service libappindicator1 libc6
libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgdk-
pixbuf2.0-0 libglib2.0-0 libnspr4 libpango-1.0-0 libstdc++6 libx11-6 libxcb1
libxext6 libxfixes3 libxrender1 libxtst6 ca-certificates fonts-liberation lsb-
release xdg-utils wget  
# Set up latest nodejs  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -y nodejs  
# Create non-root user  
RUN useradd -m puser  
USER puser  
# Create node modules folder and set NODE_PATH environment variable  
RUN mkdir -p /home/puser/node_modules  
ENV NODE_PATH /home/puppeteer/node_modules  
WORKDIR /home/puser/node_modules  
# Install webpack (dep of puppeteer)  
RUN npm i webpack  
# Clone and install puppeteer  
RUN git clone https://github.com/GoogleChrome/puppeteer  
WORKDIR /home/puser/node_modules/puppeteer  
RUN npm i .  
# Go to examples folder  
WORKDIR /home/puser/node_modules/puppeteer/examples  
# Add no-sandbox argument  
RUN perl -p -i -e "s/puppeteer.launch\\(\\)/puppeteer.launch({args: ['--no-
sandbox']})/" *  
CMD echo 'eg: node pdf.js' && bash  
  

