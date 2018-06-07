# Bundle APP files  
FROM ubuntu:14.04  
RUN apt-get -qq update && apt-get -qq -y upgrade  
RUN apt-get -qq -y install wget  
RUN wget
https://downloadarchive.documentfoundation.org/libreoffice/old/5.3.2.2/deb/x86_64/LibreOffice_5.3.2.2_Linux_x86-64_deb.tar.gz  
RUN apt-get install -qq -y libxinerama1 libfontconfig1 libdbus-glib-1-2
libcairo2 libcups2 libglu1-mesa libsm6  
RUN tar -zxvf LibreOffice_5.3.2.2_Linux_x86-64_deb.tar.gz  
RUN ls LibreOffice_5.3.2.2_Linux_x86-64_deb/DEBS  
RUN cd LibreOffice_5.3.2.2_Linux_x86-64_deb/DEBS && dpkg -i *.deb && apt-get
-f install  
RUN apt-get install -qq -y ttf-mscorefonts-installer  
RUN apt-get install -qq -y fonts-wqy-zenhei  
RUN apt-get install -qq -y build-essential  
  
# Install Node.js >= 8.x  
RUN apt-get install -qq -y curl  
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -  
RUN apt-get install -qq -y nodejs  
  
# Set environment variables  
ENV appDir /srv/backend  
  
# Set the work directory  
WORKDIR ${appDir}  
  
# Add our package.json and install *before* adding our application files  
ADD package.json ./  
RUN npm i --production  
  
# Install pm2 so we can run our application  
RUN npm i -g pm2  
  
#Add application files  
ADD . ./  
  
EXPOSE 8081  
CMD ["pm2", "start", "pm2.json", "--env=production", "--no-daemon"]  

