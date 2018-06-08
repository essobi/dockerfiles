FROM microsoft/aspnetcore-build:1.1.8-1.1.9  
WORKDIR /pipeline  
  
COPY ./pipeline/shared .  
COPY ./pipeline/dotnet .  
  
RUN apt-get update --quiet && apt-get install -y --no-install-recommends
--quiet zip jq lftp  
RUN npm install -g azure-cli --silent

