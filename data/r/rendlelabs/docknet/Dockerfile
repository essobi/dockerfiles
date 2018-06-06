FROM ubuntu:trusty  
  
# Install dotnet-nightly  
RUN sh -c 'echo "deb [arch=amd64] http://apt-
mo.trafficmanager.net/repos/dotnet/ trusty main" >
/etc/apt/sources.list.d/dotnetdev.list' \  
&& apt-key adv --keyserver apt-mo.trafficmanager.net --recv-keys 417A0893 \  
&& apt-get update \  
&& apt-get install -y dotnet-nightly \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
COPY dotnetproxy /usr/local/bin/  
ENTRYPOINT ["dotnetproxy"]

