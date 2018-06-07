FROM tagplus5/nodejs:6-16.04-tm  
  
RUN DEBIAN_FRONTEND=noninteractive && \  
rm -rf /var/lib/apt/lists/* && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \  
echo "deb http://download.mono-project.com/repo/debian wheezy main" | tee
/etc/apt/sources.list.d/mono-xamarin.list && \  
bash -c 'echo "deb [arch=amd64] https://apt-
mo.trafficmanager.net/repos/dotnet-release/ xenial main" >
/etc/apt/sources.list.d/dotnetdev.list' && \  
apt-key adv --keyserver apt-mo.trafficmanager.net --recv-keys 417A0893 && \  
apt-get update && apt-get -y upgrade && \  
apt-get install -y --no-install-recommends mono-devel ca-certificates-mono
nuget dotnet-dev-1.0.0-preview2-003131 python g++ && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* && \  
git clone https://github.com/tjanczuk/edge.git && \  
cd edge && \  
yarn && \  
yarn cache clean  
  
CMD [ "node", "/root/edge/samples/101_hello_lambda.js" ]  

