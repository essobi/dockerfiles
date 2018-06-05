FROM microsoft/aspnetcore-build:lts  
MAINTAINER Eduardo Sousa <ecsousa@gmail.com>  
  
# Configure mono's apt channel  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF\  
&& echo "deb http://download.mono-project.com/repo/debian jessie main" >>
/etc/apt/sources.list.d/mono-official.list\  
# Update source  
&& apt-get update\  
&& apt-get install --no-install-recommends\  
# Install mono, as Cake's dependencyy  
mono-devel\  
# Install build-essential for node's native modulesj  
build-essential\  
-y\  
# Install SQL Server's client  
&& npm install -g sql-cli\  
# cleanning up  
&& apt-get clean\  
&& rm -rf /var/lib/apt/lists/* /tmp/*  

