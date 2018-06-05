FROM debian:wheezy  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections \  
&& echo "deb http://http.debian.net/debian wheezy-backports main" >
/etc/apt/sources.list.d/wheezy-backports.list \  
&& apt-get update \  
&& apt-get install -y wget curl apt-utils \  
&& apt-get -t wheezy-backports install -y git \  
&& apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \  
&& echo "deb http://download.mono-project.com/repo/debian
wheezy/snapshots/4.0.0 main" > /etc/apt/sources.list.d/mono-xamarin.list \  
&& echo "deb http://download.mono-project.com/repo/debian alpha main" >
/etc/apt/sources.list.d/mono-xamarin-alpha.list \  
&& apt-get update \  
&& apt-get install -y mono-devel ca-certificates-mono fsharp mono-vbnc
libgdiplus \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

