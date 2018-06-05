FROM debian:wheezy  
  
MAINTAINER Botlink <talk@botlink.io>  
  
#based on dockerfile by Michael Friis <friism@gmail.com>  
RUN apt-get update \  
&& apt-get install -y curl \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF  
  
RUN echo "deb http://download.mono-project.com/repo/debian alpha main" >
/etc/apt/sources.list.d/mono-xamarin.list \  
&& apt-get update \  
&& apt-get install -y mono-devel ca-certificates-mono nuget \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /usr/src/app/source /usr/src/app/build  
WORKDIR /usr/src/app/source  
  
RUN printf 'nameserver 8.8.8.8\nnameserver 8.8.4.4' > /etc/resolv.conf  
  
RUN mozroots --machine --import --sync --quiet  

