  
FROM strongandstable/docker-nodejs  
  
  
# == Installs latest version of PhoneGap  
# This forces cordova to build the android fakeapp whitout triggering the
license agreement which we already accepted.  
RUN mkdir "$ANDROID_HOME/licenses" && \  
echo -e "\n8933bad161af4178b1185d1a37fbf41ea5269c55" >
"$ANDROID_HOME/licenses/android-sdk-license" && \  
echo -e "\n84831b9409646a918e30573bab4c9c91346d8abd" >
"$ANDROID_HOME/licenses/android-sdk-preview-license"  
  
# Forces a create and build in order to preload libraries  
RUN npm install -g phonegap@latest && \  
npm install -g xmldom && \  
npm install -g xpath && \  
cd /tmp && \  
phonegap create fakeapp && \  
cd /tmp/fakeapp && \  
phonegap build android && \  
cd && \  
rm -rf /tmp/fakeapp  
  
VOLUME ["/data"]  
WORKDIR /data  
  
EXPOSE 3000  

