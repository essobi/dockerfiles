FROM ubuntu:14.04  
MAINTAINER George Dernikos <geoder101@gmail.com>  
  
ENV DOCKER_CONTAINER=1 \  
DEBIAN_FRONTEND=noninteractive  
  
RUN apt-key adv \  
\--keyserver hkp://keyserver.ubuntu.com:80 \  
\--recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \  
echo "deb http://download.mono-project.com/repo/debian wheezy main" \  
> /etc/apt/sources.list.d/mono-xamarin.list  
  
RUN apt-get update \  
&& apt-get install -yq mono-complete fsharp \  
&& apt-get clean  
  
RUN mozroots --import --sync \  
&& yes | certmgr -ssl https://go.microsoft.com \  
&& yes | certmgr -ssl https://nugetgallery.blob.core.windows.net \  
&& yes | certmgr -ssl https://nuget.org  
  
RUN ln -s /usr/lib/mono /usr/local/lib/mono  
  
WORKDIR /root  
  
CMD ["fsharpi"]  

