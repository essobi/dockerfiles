FROM circleci/android:api-26-alpha  
MAINTAINER daniel@qixxit.de  
  
USER root  
RUN apt-get update && apt-get install --no-install-recommends -y ruby ruby-dev
build-essential \  
&& gem install fastlane --no-rdoc --no-ri --no-document --quiet \  
&& apt-get autoremove -y && rm -rf /var/lib/apt/lists/*  
USER circleci  

