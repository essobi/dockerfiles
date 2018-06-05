#based on
https://www.hanselman.com/blog/TryingOutNewNETCoreAlpineDockerImages.aspx  
FROM microsoft/dotnet:2.0-sdk as builder  
  
RUN mkdir -p /root/src/app/DotnetHttpDevNull  
WORKDIR /root/src/app/DotnetHttpDevNull  
  
COPY DotnetHttpDevNull.csproj .  
RUN dotnet restore ./DotnetHttpDevNull.csproj  
  
COPY . .  
RUN dotnet publish -c release -o published  
  
FROM microsoft/aspnetcore  
  
WORKDIR /root/  
COPY \--from=builder /root/src/app/DotnetHttpDevNull/published .  
ENV ASPNETCORE_URLS=http://+:5000  
EXPOSE 5000/tcp  
CMD ["dotnet", "./DotnetHttpDevNull.dll"]

