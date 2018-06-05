FROM microsoft/aspnetcore:2.0 AS base  
WORKDIR /app  
ARG source  
RUN apt-get update  
RUN apt-get install -y libgdiplus  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
EXPOSE 80  
# build backend  
FROM microsoft/aspnetcore-build:2.0 AS build  
WORKDIR /src  
COPY server .  
RUN dotnet restore -nowarn:msb3202,nu1503  
WORKDIR /src  
RUN dotnet build -c Release -o /app  
  
FROM build AS publish  
RUN dotnet publish -c Release -o /app  
  
# build frontend  
FROM node:8.11.1-alpine as ng  
COPY ./client/package.json ./client/package-lock.json ./  
RUN yarn && mkdir /ng-app && cp -R ./node_modules ./ng-app  
WORKDIR /ng-app  
COPY client .  
RUN yarn run build  
  
# finalize  
FROM base AS final  
WORKDIR /app  
COPY \--from=publish /app .  
COPY \--from=ng /ng-app/dist wwwroot  
ENTRYPOINT ["dotnet", "Server.dll"]  

