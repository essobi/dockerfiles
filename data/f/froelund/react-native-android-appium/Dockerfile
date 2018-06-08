FROM bitriseio/docker-android  
  
RUN apt-get update -qq  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs build-essential  
RUN yarn global add wdio@1.0.3 appium@1.7.1

