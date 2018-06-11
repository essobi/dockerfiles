FROM microsoft/aspnetcore-build:2.0.0  
  
RUN apt-get update \  
&& apt-get install -y libfontconfig openssh-client dos2unix rsync git \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p ~/.ssh  

