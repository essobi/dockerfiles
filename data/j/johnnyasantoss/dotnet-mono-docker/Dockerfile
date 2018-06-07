FROM microsoft/dotnet:2.0-runtime  
  
LABEL maintainer "Johnny Santos <johnnyadsantos@gmail.com>"  
  
RUN apt-get update -y \  
&& apt-get install \  
gnupg \  
gnupg1 \  
gnupg2 \  
dirmngr \  
-y \  
\--no-install-recommends \  
\--no-install-suggests  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \  
&& echo "deb http://download.mono-project.com/repo/debian
stretch/snapshots/5.2.0 main" | tee -a /etc/apt/sources.list.d/mono-
xamarin.list  
  
RUN apt-get update -y \  
&& apt-get install \  
-y \  
\--no-install-recommends \  
\--no-install-suggests \  
mono-devel \  
mono-xsp4 \  
ca-certificates-mono \  
referenceassemblies-pcl \  
nuget \  
&& nuget update -Self \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get autoremove -y \  
&& apt-get autoclean -y \  
&& mkdir /var/www  
  
WORKDIR /var/www  
  
VOLUME /var/www  

