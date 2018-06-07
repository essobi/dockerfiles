FROM node  
  
# MAINTAINER Jo Shields <jo.shields@xamarin.com>  
# MAINTAINER Alexander Köplinger <alkpli@microsoft.com>  
  
ENV MONO_VERSION 5.4.1.6  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF  
  
RUN echo "deb http://download.mono-project.com/repo/debian
jessie/snapshots/$MONO_VERSION main" > /etc/apt/sources.list.d/mono-
official.list \  
&& apt-get update \  
&& apt-get install -y \  
mono-runtime \  
binutils \  
curl \  
mono-devel \  
ca-certificates-mono \  
fsharp \  
mono-vbnc \  
nuget \  
referenceassemblies-pcl \  
libc6 \  
libcurl3 \  
libgcc1 \  
libgssapi-krb5-2 \  
libicu52 \  
liblttng-ust0 \  
libssl1.0.0 \  
libstdc++6 \  
libunwind8 \  
libuuid1 \  
zlib1g \  
&& rm -rf /var/lib/apt/lists/* /tmp/*  
  
# Install .NET Core SDK  
ENV DOTNET_SDK_VERSION 2.0.3  
ENV DOTNET_SDK_DOWNLOAD_URL
https://dotnetcli.blob.core.windows.net/dotnet/Sdk/$DOTNET_SDK_VERSION/dotnet-
sdk-$DOTNET_SDK_VERSION-linux-x64.tar.gz  
ENV DOTNET_SDK_DOWNLOAD_SHA
74A0741D4261D6769F29A5F1BA3E8FF44C79F17BBFED5E240C59C0AA104F92E93F5E76B1A262BDFAB3769F3366E33EA47603D9D725617A75CAD839274EBC5F2B  
  
RUN curl -SL $DOTNET_SDK_DOWNLOAD_URL --output dotnet.tar.gz \  
&& echo "$DOTNET_SDK_DOWNLOAD_SHA dotnet.tar.gz" | sha512sum -c - \  
&& mkdir -p /usr/share/dotnet \  
&& tar -zxf dotnet.tar.gz -C /usr/share/dotnet \  
&& rm dotnet.tar.gz \  
&& ln -s /usr/share/dotnet/dotnet /usr/bin/dotnet  
  
# Trigger the population of the local package cache  
ENV NUGET_XMLDOC_MODE skip  
RUN mkdir warmup \  
&& cd warmup \  
&& dotnet new \  
&& cd .. \  
&& rm -rf warmup \  
&& rm -rf /tmp/NuGetScratch

