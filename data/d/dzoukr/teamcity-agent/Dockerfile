FROM sjoerdmulder/teamcity-agent:latest  
  
MAINTAINER Roman Provaznik <dzoukr@dzoukr.cz>  
  
# INSTALL MONO  
RUN apt-get update \  
&& apt-get install -y curl \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF  
  
RUN echo "deb http://download.mono-project.com/repo/debian
wheezy/snapshots/4.4.0.182 main" > /etc/apt/sources.list.d/mono-xamarin.list \  
&& apt-get update \  
&& apt-get install -y mono-devel ca-certificates-mono fsharp mono-vbnc nuget
referenceassemblies-pcl \  
&& rm -rf /var/lib/apt/lists/*  
# INSTALL LEIN  
ENV LEIN_ROOT 1  
RUN curl -L -s
https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein > \  
/usr/local/bin/lein \  
&& chmod 0755 /usr/local/bin/lein \  
&& lein upgrade  

