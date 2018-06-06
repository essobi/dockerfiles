FROM microsoft/dotnet:1-sdk  
MAINTAINER codedevote@gmail.com  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \  
&& echo "deb http://download.mono-project.com/repo/debian jessie main" | tee
/etc/apt/sources.list.d/mono-official.list \  
&& apt-get update && apt-get upgrade -y  
  
RUN apt-get update && apt-get install -y \--fix-missing mono-complete nuget  

