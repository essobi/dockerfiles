# Example from AZ  
FROM microsoft/dotnet:1.0.1-sdk-projectjson  
MAINTAINER "AZ"  
COPY ["./src/MVC5ForLinuxTest2/", "/app"]  
COPY ["./start.sh", "."]  
RUN chmod +x ./start.sh  
HEALTHCHECK CMD curl --fail http://localhost:5001/api/datetimeutc || exit 1  
CMD ["./start.sh"]  

