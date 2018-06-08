FROM microsoft/aspnetcore-build AS builder  
RUN npm install --global yarn  
WORKDIR .  
COPY . .  
RUN dotnet restore  
WORKDIR ./src/Obsidian  
RUN yarn && dotnet publish --output /app/ --configuration Release  
  
FROM microsoft/aspnetcore  
MAINTAINER ZA-PT  
WORKDIR /app  
COPY \--from=builder /app .  
EXPOSE 80  
ENTRYPOINT ["dotnet", "Obsidian.dll"]  

