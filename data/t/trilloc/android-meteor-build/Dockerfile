FROM beevelop/android-nodejs:latest  
  
RUN curl https://install.meteor.com/ | sh  
  
RUN apt-get update && apt-get install -y git \  
&& echo y | android update sdk --no-ui --all \--filter "extra-
android-m2repository" \  
&& echo y | android update sdk --no-ui --all \--filter "extra-google-
google_play_services" \  
&& echo y | android update sdk --no-ui --all \--filter "extra-
google-m2repository" \  
&& echo y | android update sdk --no-ui --all \--filter "extra-android-support"  
  
RUN npm install -g cordova \  
&& npm install -g mup@latest \  
&& npm install -g ssh2  

