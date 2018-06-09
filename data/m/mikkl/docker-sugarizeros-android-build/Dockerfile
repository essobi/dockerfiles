FROM beevelop/ionic  
RUN apt-get update  
RUN apt-get install git -y  
RUN cordova telemetry off  
WORKDIR /  
CMD bash -c "if [ ! -d "sugarizer" ]; then git clone
https://github.com/llaske/sugarizer.git; fi;\  
cd sugarizer;\  
cd /; \  
cordova create sugar-cordova; \  
cd sugar-cordova; \  
cordova platform add android; \  
cordova plugin add https://github.com/llaske/cordova-plugin-sugarizeros.git; \  
rm config.xml; \  
rm -fr www; \  
cp -R /sugarizer www; \  
mv www/res .; \  
cp www/config.xml .;\  
cordova run; \  
cp /sugar-cordova/platforms/android/build/outputs/apk/android-debug.apk
/output/android-debug.apk"  

