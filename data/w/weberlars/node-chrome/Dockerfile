FROM node:slim  
  
ENV CHROME_PACKAGE="google-chrome-stable_58.0.3029.81-1_amd64.deb"  
RUN apt-get update && \  
apt-get install -y unzip xvfb wget && \  
wget https://github.com/webnicer/chrome-
downloads/raw/master/x64.deb/${CHROME_PACKAGE} && \  
dpkg --unpack ${CHROME_PACKAGE} && \  
apt-get install -y -f && \  
rm ${CHROME_PACKAGE} && \  
rm -rf /var/lib/apt/lists/*

