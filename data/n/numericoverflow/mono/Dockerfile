FROM 32bit/debian  
  
MAINTAINER Fecana  
  
RUN apt-get update  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF  
  
RUN echo "deb http://download.mono-project.com/repo/debian wheezy main" >
/etc/apt/sources.list.d/mono-xamarin.list \  
&& apt-get update \  
&& echo "deb http://download.mono-project.com/repo/debian wheezy-
apache24-compat main" >> /etc/apt/sources.list.d/mono-xamarin.list \  
&& echo "deb http://download.mono-project.com/repo/debian wheezy-
libjpeg62-compat main" >> /etc/apt/sources.list.d/mono-xamarin.list \  
&& apt-get update \  
&& apt-get install -y mono-devel mono-vbnc nuget build-essential  
  
EXPOSE 12345  

