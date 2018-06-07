FROM ubuntu:xenial  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \  
&& echo "deb http://download.mono-project.com/repo/debian xenial/snapshots/5.2
main" > /etc/apt/sources.list.d/mono-xamarin.list  
RUN apt-get update \  
&& apt-get install -y mono-devel nuget tzdata \  
&& rm -rf /var/lib/apt/lists/*  

