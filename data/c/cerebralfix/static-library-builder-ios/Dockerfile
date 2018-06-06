FROM cerebralfix/static-library-builder-base  
  
RUN get-source ios-headers https://github.com/MP0w/iOS-Headers.git
67da653b7f8b72a93af4db40d45acb639954a777  
  
WORKDIR /opt/src/ios-headers/iOS8.1/Frameworks/  
  
RUN for FRAMEWORK in *; do \  
mkdir -p /opt/ios-sdk/System/Library/Frameworks/$FRAMEWORK/Headers/; \  
cp -r $FRAMEWORK/* /opt/ios-sdk/System/Library/Frameworks/$FRAMEWORK/Headers/;
\  
done  
  
ENV IPHONEOS_DEPLOYMENT_TARGET 8.1  
ENV CC clang  
ENV CFLAGS -isysroot /opt/ios-sdk/  
ENV LDFLAGS -isysroot /opt/ios-sdk/  
  
RUN mkdir -p
/opt/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/
&& \  
ln -s /opt/ios-sdk/
/opt/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS8.1.dk  
  
ADD xcode-select /usr/bin/  
ADD xcrun /usr/bin/  
RUN chmod +x /usr/bin/xcode-select && chmod +x /usr/bin/xcrun  

