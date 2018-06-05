FROM microsoft/dotnet:1.0.0-preview2-sdk  
  
# Set the Working Directory  
WORKDIR /app  
  
# Copy the app  
COPY /src /app  
  
RUN dotnet restore  
  
WORKDIR /app/FindWifesPhoneDNX.Console  
  
RUN dotnet build -c Release  
# Start the app  
ENTRYPOINT dotnet bin/Release/netcoreapp1.0/FindWifesPhoneDNX.Console.dll  

