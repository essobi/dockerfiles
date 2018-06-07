FROM ubuntu:15.10  
  
ENV SWIFT_DOWNLOAD_URL https://swift.org/builds/development/ubuntu1510/swift-
DEVELOPMENT-SNAPSHOT-2016-01-25-a/swift-DEVELOPMENT-
SNAPSHOT-2016-01-25-a-ubuntu15.10.tar.gz  
ENV SWIFT_DOWNLOAD_FILENAME swift-DEVELOPMENT-
SNAPSHOT-2016-01-25-a-ubuntu15.10  
ENV SWIFT_INSTALL_PATH /usr/local  
ENV PATH $SWIFT_INSTALL_PATH/swift/usr/bin:$PATH  
  
RUN true \  
&& apt-get update \  
&& apt-get install -y \  
clang \  
libicu-dev \  
libpython2.7-dev \  
libxml2 \  
curl \  
git \  
\  
&& mkdir -p $SWIFT_INSTALL_PATH \  
&& cd $SWIFT_INSTALL_PATH \  
&& echo Downloading: $SWIFT_DOWNLOAD_URL \  
&& curl -O $SWIFT_DOWNLOAD_URL \  
&& echo Downloading: $SWIFT_DOWNLOAD_URL.sig \  
&& curl -O $SWIFT_DOWNLOAD_URL.sig \  
&& gpg --keyserver hkp://pool.sks-keyservers.net --recv-keys \  
'7463 A81A 4B2E EA1B 551F FBCF D441 C977 412B 37AD' \  
'1BE1 E29A 084C B305 F397 D62A 9F59 7F4D 21A5 6D5F' \  
&& gpg --verify $SWIFT_DOWNLOAD_FILENAME.tar.gz.sig \  
&& rm $SWIFT_DOWNLOAD_FILENAME.tar.gz.sig \  
&& tar -xzf $SWIFT_DOWNLOAD_FILENAME.tar.gz \  
&& rm $SWIFT_DOWNLOAD_FILENAME.tar.gz \  
&& ln -s $SWIFT_DOWNLOAD_FILENAME swift \  
\  
&& apt-get purge -y \  
curl \  
&& apt-get autoremove -y \  
&& apt-get clean -y \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

