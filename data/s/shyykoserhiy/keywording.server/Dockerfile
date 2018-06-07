FROM jrottenberg/ffmpeg  
##dotnet  
# Work around https://github.com/dotnet/cli/issues/1582 until Docker releases
a  
# fix (https://github.com/docker/docker/issues/20818). This workaround allows  
# the container to be run with the default seccomp Docker settings by avoiding  
# the restart_syscall made by LTTng which causes a failed assertion.  
ENV LTTNG_UST_REGISTER_TIMEOUT 0  
# Install .NET CLI dependencies  
RUN apt-get update  
RUN apt-get install -y apt-transport-https  
RUN sh -c 'echo "deb [arch=amd64] https://apt-
mo.trafficmanager.net/repos/dotnet-release/ xenial main" >
/etc/apt/sources.list.d/dotnetdev.list'  
RUN apt-key adv --keyserver apt-mo.trafficmanager.net --recv-keys 417A0893  
RUN apt-get update  
RUN apt-get install -y dotnet-dev-1.0.0-preview2-003121  
  
###  
COPY . /app  
  
WORKDIR /app  
  
RUN ["dotnet", "restore"]  
  
RUN ["dotnet", "build"]  
  
EXPOSE 5000/tcp  
  
ENTRYPOINT ["dotnet", "run", "--server.urls", "http://0.0.0.0:5000"]  

