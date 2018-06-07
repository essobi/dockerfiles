FROM jetbrains/teamcity-agent:latest  
  
RUN sh -c 'echo "deb [arch=amd64] https://apt-
mo.trafficmanager.net/repos/dotnet-release/ xenial main" >
/etc/apt/sources.list.d/dotnetdev.list' \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys 417A0893
\  
&& apt-get update \  
&& apt-get install -y dotnet-dev-1.0.1  
  
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl
-s https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl \  
&& chmod +x ./kubectl \  
&& mv ./kubectl /usr/local/bin/kubectl

