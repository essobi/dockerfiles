FROM microsoft/aspnetcore:2.0 AS base  
  
RUN apt-get update  
RUN apt-get install -y nginx  
  
WORKDIR /app  
ENV ASPNETCORE_URLS http://+:50025  
EXPOSE 50025 80  
FROM microsoft/aspnetcore-build:2.0 AS build  
WORKDIR /src  
COPY *.sln ./  
COPY Web/Web.csproj Web/  
COPY ApplicationInfrastructure/ApplicationInfrastructure.csproj
ApplicationInfrastructure/  
COPY ApplicationCore/ApplicationCore.csproj ApplicationCore/  
RUN dotnet restore  
COPY . .  
WORKDIR /src/Web  
RUN dotnet build -c Release -o /app  
  
FROM build AS publish  
RUN dotnet publish -c Release -o /app  
  
FROM base AS final  
WORKDIR /app  
COPY \--from=publish /app .  
  
COPY ./startup.sh .  
RUN chmod 755 /app/startup.sh  
  
RUN rm /etc/nginx/nginx.conf  
COPY Nginx/nginx.conf /etc/nginx/  
COPY Nginx/lanchessw.conf /etc/nginx/conf.d/  
  
CMD ["sh", "/app/startup.sh"]  

