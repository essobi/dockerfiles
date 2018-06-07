FROM mikewright/docker-dev-base  
  
# Install Dependencies  
RUN sudo apt-get update && \  
sudo apt-get install -y libxml2-dev clang libicu55 libpython2.7 && \  
sudo docker-cleanup  
  
# Install Swift keys  
RUN curl -sSL https://swift.org/keys/all-keys.asc | sudo gpg --import - && \  
sudo gpg --keyserver hkp://pool.sks-keyservers.net --refresh-keys Swift  
  
ENV SWIFT_BUILD_URL
https://swift.org/builds/swift-2.2.1-release/ubuntu1510/swift-2.2.1-RELEASE/swift-2.2.1-RELEASE-
ubuntu15.10.tar.gz  
ENV SWIFT_ARCHIVE_NAME swift-2.2.1-RELEASE-ubuntu15.10  
# Download and install Swift  
RUN curl -sSL $SWIFT_BUILD_URL | sudo tar -xvz -C / --strip 1  
  
ADD vimrc.bundles.local $HOME/.vimrc.bundles.local  
RUN update-vim  
  
#RUN wget $SWIFT_BUILD_URL && \  
# wget $SWIFT_BUILD_URL.sig && \  
# sudo gpg --verify $SWIFT_ARCHIVE_NAME.tar.gz.sig && \  
# sudo tar -xvzf $SWIFT_ARCHIVE_NAME.tar.gz -C / --strip 1 && \  
# sudo rm -rf $SWIFT_ARCHIVE_NAME* /tmp/* /var/tmp/*  
#Building a webserver? Expose Port 80 by uncommenting the following.  
#Expose 80  

