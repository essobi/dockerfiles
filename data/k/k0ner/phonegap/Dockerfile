FROM k0ner/nodejs-android  
  
# Installs PhoneGap  
# Forces a create and build in order to preload libraries  
RUN npm install -g npm && \  
npm install -g phonegap && \  
npm install -g xmldom && \  
cd /tmp && \  
phonegap create fakeapp && \  
cd /tmp/fakeapp && \  
phonegap build android && \  
cd && \  
rm -rf /tmp/fakeapp  
  
VOLUME ["/data"]  
WORKDIR /data  
  
EXPOSE 3000  

