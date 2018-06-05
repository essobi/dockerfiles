FROM microsoft/dotnet:2-sdk  
  
EXPOSE 5000  
ADD . /wax  
  
WORKDIR /wax  
  
RUN dotnet restore --no-cache WaxAccess && dotnet publish WaxAccess -o ../bin
-c Release && rm -Rf /root/.nuget  
  
CMD dotnet bin/WaxAccess.dll  

