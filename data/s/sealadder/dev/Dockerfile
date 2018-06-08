# FROM microsoft/dotnet:latest  
FROM sealadder/sealadderbuild:1.1.7  
ENV ASPNETCORE_ENVIRONMENT Production  
# ENV ASPNETCORE_ENVIRONMENT Staging  
RUN apt-get install curl unzip -y  
# following here because of : https://github.com/phusion/baseimage-
docker/issues/319  
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils  
RUN curl -sSL https://aka.ms/getvsdbgsh | bash /dev/stdin -v latest -l ~/vsdbg  
  
COPY . /app  
WORKDIR /app/SEALadder  
RUN ["npm", "-v"]  
RUN ["node", "-v"]  
RUN ["dotnet", "--version"]  
RUN ["npm", "install"]  
RUN ["dotnet", "restore"]  
RUN ["dotnet", "build"]  
  
RUN ["webpack", "--config", "webpack.config.vendor.js", "--env.prod"]  
RUN ["webpack", "--env.prod"]  
  
EXPOSE 5000/tcp  
  
ENTRYPOINT ["./run-server.sh"]  

