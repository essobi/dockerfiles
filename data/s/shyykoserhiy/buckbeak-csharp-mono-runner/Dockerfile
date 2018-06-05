FROM microsoft/dotnet:1.0.0-preview2-sdk  
MAINTAINER shyyko.serhiy@gmail.com  
  
RUN mkdir /app && cd /app && dotnet new && dotnet restore  
WORKDIR /app  
  
#https://github.com/mono/docker/blob/e92989ade1408fd977b3a15eec3c3b7a5611bcee/4.4.0.182/Dockerfile  
RUN apt-get update \  
&& apt-get install -y curl \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF  
  
RUN echo "deb http://download.mono-project.com/repo/debian
wheezy/snapshots/4.4.0.182 main" > /etc/apt/sources.list.d/mono-xamarin.list \  
&& echo "deb http://download.mono-project.com/repo/debian wheezy-
libjpeg62-compat main" | tee -a /etc/apt/sources.list.d/mono-xamarin.list \  
&& apt-get update \  
&& apt-get install -y mono-devel ca-certificates-mono fsharp mono-vbnc nuget
referenceassemblies-pcl \  
&& rm -rf /var/lib/apt/lists/*  
#https://github.com/mono/docker/blob/e92989ade1408fd977b3a15eec3c3b7a5611bcee/4.4.0.182/Dockerfile  
COPY ./run.sh /app  
  
#dotnet core  
#CMD dotnet build > /dev/null && dotnet bin/Debug/netcoreapp1.0/app.dll  
#mono  
#CMD mcs Program.cs && mono Program.exe  
ENTRYPOINT ["./run.sh"]  

