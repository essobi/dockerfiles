FROM microsoft/dotnet:2-sdk  
  
EXPOSE 5000  
ADD . /wax  
  
WORKDIR /wax  
  
RUN apt-get update && apt-get install -y libc6-dev libgdiplus  
RUN dotnet restore --no-cache WaxCrossword && dotnet publish WaxCrossword -o
../bin -c Release && rm -Rf /root/.nuget  
RUN ln -s /wax/WaxCrossword/english.json /wax/english.json  
CMD dotnet bin/WaxCrossword.dll  

