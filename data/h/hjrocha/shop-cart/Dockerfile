FROM microsoft/aspnetcore:2.0 AS base  
WORKDIR /app  
EXPOSE 80  
FROM microsoft/aspnetcore-build:2.0 AS build  
WORKDIR /src  
COPY *.sln ./  
COPY ShopCart.REST/ShopCart.REST.csproj ShopCart.REST/  
COPY ShopCart.Model/ShopCart.Model.csproj ShopCart.Model/  
RUN dotnet restore  
  
COPY . .  
WORKDIR /src/ShopCart.REST  
RUN dotnet build -c Release -o /app  
  
FROM build AS publish  
RUN dotnet publish -c Release -o /app  
  
FROM base AS final  
WORKDIR /app  
COPY \--from=publish /app .  
ENTRYPOINT ["dotnet", "ShopCart.REST.dll"]  

