# a easy way to build firefly android app from latest source  
FROM beevelop/android-nodejs:8  
MAINTAINER overcat <https://github.com/overcat>  
  
ENV CI=true  
  
RUN apt-get update && apt-get install -y --no-install-recommends python gcc
g++ make && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean  
  
WORKDIR /  
  
RUN echo "git clone https://github.com/StellarCN/firefly.git && \  
cd firefly && \  
npm install -g cordova && \  
npm install && \  
npm run build && \  
cordova platform add android && \  
cordova build android && \  
cp -r platforms/android/build/outputs/apk/debug/ /fireflyapk" > build.sh  
  
CMD ["/bin/bash", "/build.sh"]  

