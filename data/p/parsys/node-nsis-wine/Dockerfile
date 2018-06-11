FROM node  
  
RUN dpkg --add-architecture i386 \  
&& apt -qq update \  
&& apt -qq upgrade -y \  
&& apt -qq install -y nsis vim wine wine32 \  
&& rm -rf /var/lib/apt/lists/*  

