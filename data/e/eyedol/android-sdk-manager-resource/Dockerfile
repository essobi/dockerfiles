FROM java:8-jdk  
  
RUN mkdir -p /opt/resource \  
&& curl -L "https://dl.google.com/android/repository/sdk-tools-
linux-3859397.zip" \  
> /opt/resource/android-sdk-linux.zip  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends jq expect zip unzip ansible \  
&& rm -rf /var/lib/apt/lists/*  

