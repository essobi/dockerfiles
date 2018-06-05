# Use MS.net core debian container  
FROM microsoft/dotnet:1.1.0-sdk-projectjson  
  
# Copy all the custom configurations to /bv on docker image  
COPY . /Broadvoice  
  
# install mono first  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \  
&& echo "deb http://download.mono-project.com/repo/debian wheezy main" | tee
/etc/apt/sources.list.d/mono-xamarin.list \  
&& echo "deb http://download.mono-project.com/repo/debian wheezy-
libjpeg62-compat main" | tee -a /etc/apt/sources.list.d/mono-xamarin.list \  
&& apt-get update -y \  
&& apt-get install -y mono-devel  
  
# install redis then cleanup list  
RUN apt-get install -y redis-server \  
&& rm -rf /var/lib/apt/lists/*  
  
#set default environment variables  
ENV CONFIGURATION=Release \  
BUILD_VERSION=1.1.0 \  
ASPNETCORE_URLS="http://*:5000"  
# Open ports for Redis: main, cluster, sentiel  
EXPOSE 5000/tcp 6379/tcp 16379 26379  
# start redis  
RUN service redis-server start \  
&& service redis-server status \  
&& redis-cli ping  

