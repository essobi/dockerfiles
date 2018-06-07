FROM travix/base-debian:latest  
  
MAINTAINER Travix  
  
# build time environment variables  
ENV DOTNET_CORE_VERSION=1.0.0-rc2-3002702  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libc6 \  
libcurl3 \  
libgcc1 \  
libicu52 \  
liblttng-ust0 \  
libssl1.0.0 \  
libstdc++6 \  
libtinfo5 \  
libunwind8 \  
libuuid1 \  
zlib1g \  
ca-certificates \  
xz-utils \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN curl -SL
https://dotnetcli.blob.core.windows.net/dotnet/beta/Binaries/$DOTNET_CORE_VERSION/dotnet-
debian-x64.$DOTNET_CORE_VERSION.tar.gz --output dotnet.tar.gz \  
&& mkdir -p /usr/share/dotnet \  
&& tar -zxf dotnet.tar.gz -C /usr/share/dotnet \  
&& rm dotnet.tar.gz \  
&& ln -s /usr/share/dotnet/dotnet /usr/bin/dotnet  
  
RUN mkdir -p /dotnetapp  
  
WORKDIR /dotnetapp  
  
ENTRYPOINT ["dotnet", "run"]  
  
ONBUILD COPY . /dotnetapp

