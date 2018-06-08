FROM microsoft/dotnet  
WORKDIR /app  
COPY ./EchoAPI .  
ENV ASPNETCORE_URLS http://+:5001  
EXPOSE 5001  
RUN dotnet restore  
ENTRYPOINT ["dotnet", "run"]  

