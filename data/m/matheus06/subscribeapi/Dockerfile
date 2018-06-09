FROM microsoft/aspnetcore-build:2.0 AS build-env  
WORKDIR /app  
  
# Copy csproj and restore  
COPY *.sln /.  
COPY ./src/MSAP.WebApiCore.Services.SubscribeApi/*.csproj
./MSAP.WebApiCore.Services.SubscribeApi/  
COPY ./src/MSAP.WebApiCore.Application/*.csproj ./MSAP.WebApiCore.Application/  
COPY ./src/MSAP.WebApiCore.Domain/*.csproj ./MSAP.WebApiCore.Domain/  
COPY ./src/MSAP.WebApiCore.Infra.Data/*.csproj ./MSAP.WebApiCore.Infra.Data/  
COPY ./src/MSAP.WebApiCore.Infra.CrossCutting.EventBus/*.csproj
./MSAP.WebApiCore.Infra.CrossCutting.EventBus/  
COPY ./src/MSAP.WebApiCore.Infra.CrossCutting.EventBusRabbitMQ/*.csproj
./MSAP.WebApiCore.Infra.CrossCutting.EventBusRabbitMQ/  
COPY ./src/MSAP.WebApiCore.Infra.CrossCutting.IoC/*.csproj
./MSAP.WebApiCore.Infra.CrossCutting.IoC/  
COPY ./src/MSAP.WebApiCore.Services.SubscribeApi/*.csproj
./MSAP.WebApiCore.Services.SubscribeApi/  
  
RUN dotnet restore
./MSAP.WebApiCore.Services.SubscribeApi/MSAP.WebApiCore.Services.SubscribeApi.csproj  
  
COPY ./src/MSAP.WebApiCore.Services.SubscribeApi/
./MSAP.WebApiCore.Services.SubscribeApi/  
COPY ./src/MSAP.WebApiCore.Application/ ./MSAP.WebApiCore.Application/  
COPY ./src/MSAP.WebApiCore.Domain/ ./MSAP.WebApiCore.Domain/  
COPY ./src/MSAP.WebApiCore.Infra.Data/ ./MSAP.WebApiCore.Infra.Data/  
COPY ./src/MSAP.WebApiCore.Infra.CrossCutting.EventBus/
./MSAP.WebApiCore.Infra.CrossCutting.EventBus/  
COPY ./src/MSAP.WebApiCore.Infra.CrossCutting.EventBusRabbitMQ/
./MSAP.WebApiCore.Infra.CrossCutting.EventBusRabbitMQ/  
COPY ./src/MSAP.WebApiCore.Infra.CrossCutting.IoC/
./MSAP.WebApiCore.Infra.CrossCutting.IoC/  
  
RUN dotnet publish
./MSAP.WebApiCore.Services.SubscribeApi/MSAP.WebApiCore.Services.SubscribeApi.csproj
-c Release -o out  
  
# Build runtime image  
FROM microsoft/aspnetcore:2.0  
WORKDIR /app  
COPY \--from=build-env /app/MSAP.WebApiCore.Services.SubscribeApi/out .  
ENTRYPOINT ["dotnet", "MSAP.WebApiCore.Services.SubscribeApi.dll"]  
  

