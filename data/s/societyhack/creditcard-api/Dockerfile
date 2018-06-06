FROM microsoft/aspnetcore-build:2.0 AS build-env  
WORKDIR /app  
COPY . ./  
  
# copy csproj and restore as distinct layers  
RUN dotnet restore  
#RUN dotnet test
/app/Motix.Microservice.Billing.Tests/Motix.Microservice.Billing.Tests.csproj  
# copy everything else and build  
WORKDIR /app/CreditCardAPI  
RUN dotnet publish -c Release -o out  
  
# build runtime image  
FROM microsoft/aspnetcore:2.0  
ENV ASPNETCORE_ENVIRONMENT="Development"  
WORKDIR /app  
COPY \--from=build-env /app/CreditCardAPI/out .  
ENTRYPOINT ["dotnet", "CreditCardAPI.dll"]  

