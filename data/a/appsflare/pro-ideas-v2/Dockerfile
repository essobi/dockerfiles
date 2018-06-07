#First Stage  
FROM microsoft/dotnet:1.1-sdk  
  
# create build directory and add src files  
RUN mkdir /build  
ADD src /build/src  
  
# set the work directory to build  
WORKDIR /build  
  
#Navigate to main project directory, restore dependencies and publish the
project  
RUN cd src/ProIdeas.UI && \  
dotnet restore && \  
dotnet publish -o /build/out  
  
# Second Stage  
FROM microsoft/dotnet:1.1-runtime  
EXPOSE 5000  
ENV ASPNETCORE_URLS=http://+:5000  
ENV ASPNETCORE_ENVIRONMENT=Production  
WORKDIR /app  
CMD ["dotnet", "ProIdeas.UI.dll"]  
  
COPY \--from=0 /build/out /app/

