FROM beevelop/android-nodejs:latest  
MAINTAINER Randy Stauner <randy@magnificent-tears.com>  
  
RUN apt-get update \  
&& apt-get install -y \  
g++ \  
make \  
python \  
&& rm -rf /var/lib/apt/lists/* /tmp/*  
  
# NativeScript suggests:  
# --filter tools,platform-tools,android-23,build-tools-23.0.2,extra-
android-m2repository,extra-google-m2repository,extra-android-support --all
--no-ui  
# Setup maven repo to satisfy tns doctor.  
RUN echo y | $ANDROID_HOME/tools/android update sdk --no-ui \  
\--filter tools-25.2.4,platform-tools-25.0.3,build-
tools-25.0.2,android-23,extra-android-m2repository,extra-
google-m2repository,extra-android-support  
  
RUN npm install -g nativescript --unsafe-perm  
  
# /root/.m2 ?  
VOLUME \  
/root/.android \  
/root/.gradle \  
/root/.local/share/.nativescript-cli  
  
RUN mkdir -p /src  
WORKDIR /src  

