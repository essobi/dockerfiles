FROM java:7  
ENV APKTOOL_VERSION 2.2.1  
RUN apt-get update && apt-get install -y wget && \  
wget
https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool
-O /usr/local/bin/apktool && \  
chmod a+x /usr/local/bin/apktool && \  
wget
https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_${APKTOOL_VERSION}.jar
-O /usr/local/bin/apktool_${APKTOOL_VERSION}.jar && \  
ln -snf apktool_${APKTOOL_VERSION}.jar /usr/local/bin/apktool.jar && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
CMD apktool  

