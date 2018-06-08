FROM microsoft/dotnet:1.0.0-preview2-sdk  
  
  
RUN mkdir /app  
WORKDIR /app  
RUN dotnet new  
RUN dotnet restore  
  
ADD build.sh /app  
RUN chmod +x build.sh  
RUN touch /tmp/code  
  
CMD /app/build.sh  

