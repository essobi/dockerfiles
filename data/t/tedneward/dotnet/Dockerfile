FROM microsoft/dotnet:2.0-sdk  
MAINTAINER Ted Neward <ted@tedneward.com>  
  
RUN groupadd --gid 1000 dotnet \  
&& useradd --uid 1000 --gid dotnet --shell /bin/bash --create-home dotnet  
  
RUN chown -R dotnet:dotnet /usr/local  
  
USER dotnet  
WORKDIR /home/dotnet  
  
RUN git clone https://github.com/dotnet/dotnet-docker-samples
/home/dotnet/dotnet-docker-samples  
  
ENTRYPOINT ["/bin/bash"]

