# Version 1.0  
FROM linuxserver/calibre-web  
# Set basic environment settings  
ENV \  
APP_HOME="/app/calibre-web" \  
AMAZON_KG_TAR="kindlegen_linux_2.6_i386_v2_9.tar.gz" \  
AMAZON_KG_URL="http://kindlegen.s3.amazonaws.com/kindlegen_linux_2.6_i386_v2_9.tar.gz"  
RUN \  
mkdir -p /tmp && \  
mkdir -p $APP_HOME/kindlegen && \  
curl -o /tmp/$AMAZON_KG_TAR -L $AMAZON_KG_URL && \  
tar -xzf /tmp/$AMAZON_KG_TAR -C $APP_HOME/kindlegen && \  
rm -rf /tmp  

