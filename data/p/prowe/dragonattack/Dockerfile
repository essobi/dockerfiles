FROM microsoft/dotnet:1.1-sdk  
  
ADD . /app  
  
RUN cd /app/Silo \  
&& dotnet restore \  
&& dotnet build  
  
RUN cd /app/Web \  
&& dotnet restore \  
&& dotnet build  
  

