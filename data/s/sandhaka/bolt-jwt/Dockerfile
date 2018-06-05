FROM microsoft/aspnetcore:2.1.0-preview1  
WORKDIR /app  
EXPOSE 443  
COPY obj/docker/release.tar /app  
RUN tar -xf release.tar  
  
ENTRYPOINT /bin/bash -c "dotnet BoltJwt.dll"

