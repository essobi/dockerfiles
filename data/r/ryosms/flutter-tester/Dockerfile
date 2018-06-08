FROM ubuntu:18.04  
LABEL maintainer "ryosms <ryo.sms@gmail.com>"  
  
RUN mkdir -p /work  
WORKDIR /work  
  
ENV PATH /opt/flutter/bin:${PATH}  
  
RUN apt-get update -y -q \  
&& apt-get install -y --no-install-recommends -q git curl unzip libglu1
lib32stdc++6 ca-certificates \  
&& apt-get clean \  
&& rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
RUN git clone -b dev https://github.com/flutter/flutter.git /opt/flutter \  
&& flutter doctor \  
&& flutter config --no-analytics  

