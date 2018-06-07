FROM jingqian/aspnetcore-opencv-dockers:dotnetcore-2.1.0  
LABEL eilyyy <eilyyy@outlook.com>  
ENV OPENCVSHARP_VERSION="3.4.1.20180320"  
RUN apt-get update && apt-get install -y wget unzip cmake g++ libgdiplus \  
&& wget
https://github.com/shimat/opencvsharp/archive/${OPENCVSHARP_VERSION}.zip -O
opencvsharp.zip \  
&& unzip opencvsharp.zip \  
&& cd opencvsharp-${OPENCVSHARP_VERSION}/src \  
&& cmake . \  
&& make \  
&& make install \  
&& rm -r /opencvsharp-${OPENCVSHARP_VERSION} \  
&& rm /opencvsharp.zip \  
&& apt-get remove -y cmake wget unzip g++ && apt-get -y autoremove \  
&& rm -rf /var/lib/apt/lists/*

