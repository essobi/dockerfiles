FROM selenium/standalone-chrome:3.4.0-dysprosium  
  
ENV EXT_HEADLESS_URL
https://testimstatic.blob.core.windows.net/extension/testim-headless.zip  
ENV EXT_HEADLESS_ZIP_LOC /opt/testim-headless.zip  
ENV EXT_HEADLESS_LOC /opt/testim-headless  
  
USER root  
  
RUN apt-get update -qqy \  
&& apt-get -qqy install curl \  
&& wget --no-verbose -O $EXT_HEADLESS_ZIP_LOC $EXT_HEADLESS_URL \  
&& unzip $EXT_HEADLESS_ZIP_LOC -d $EXT_HEADLESS_LOC \  
&& echo $(curl -sI -X HEAD "${EXT_HEADLESS_URL}" | tr -d '\r' | sed -En
's/^ETag: (.*)/\1/p') > /opt/testim-headless-info \  
&& rm -rf /var/lib/apt/lists/*  
  
USER seluser  

