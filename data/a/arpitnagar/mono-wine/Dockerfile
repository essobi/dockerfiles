# Run windows programs like a champion  
FROM jess/wine  
MAINTAINER Arpit Nagar <arpitgold@gmail.com>  
  
# Installing Mono  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF  
RUN echo "deb http://download.mono-project.com/repo/debian wheezy main" | tee
/etc/apt/sources.list.d/mono-xamarin.list  
RUN echo "deb http://download.mono-project.com/repo/debian wheezy-
libjpeg62-compat main" | tee -a /etc/apt/sources.list.d/mono-xamarin.list  
RUN apt-get update && apt-get install -yf mono-complete mono-devel nuget ca-
certificates-mono fsharp  
  

