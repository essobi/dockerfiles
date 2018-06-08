FROM microsoft/aspnetcore-build:1.0-projectjson as build-env  
RUN apt-get -qqy update && apt-get -qqy upgrade && apt-get -qqy install git  
RUN git clone -b cesarbs/1.0.3-docker --single-branch --depth 1
https://github.com/aspnet/MusicStore.git  
  
WORKDIR /MusicStore/src/MusicStore  
RUN dotnet restore && dotnet publish -o /www -f netcoreapp1.0  
  
FROM microsoft/aspnetcore:1.0  
WORKDIR /www  
COPY \--from=build-env /www /www  
EXPOSE 5000  
CMD ["dotnet", "MusicStore.dll" ]

