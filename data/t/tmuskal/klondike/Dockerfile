FROM mono:3.10  
RUN apt-get update \  
&& apt-get install -y unzip \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl
https://ci.appveyor.com/api/buildjobs/w3klq9g28sfd8km9/artifacts/Klondike.zip
> Klondike.zip  
  
RUN unzip Klondike.zip  
  
ADD Settings.config Settings.config  
  
CMD [ "mono", "./bin/Klondike.SelfHost.exe","--interactive","--port=8080" ]  
  

