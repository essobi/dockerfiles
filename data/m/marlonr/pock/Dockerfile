FROM microsoft/dotnet:1.1-sdk-projectjson  
WORKDIR /app  
COPY . /app  
RUN dotnet restore  
EXPOSE 5000  
CMD [ "dotnet", "run" ]  

