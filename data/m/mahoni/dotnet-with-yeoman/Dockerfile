FROM node:7.3.0  
MAINTAINER mahmut Gundogdu <mahmutgundogdu@hotmail.com.tr>  
#RUN apt-get update  
# Install .NET CLI dependencies  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
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
&& rm -rf /var/lib/apt/lists/*  
  
# Install .NET Core SDK  
ENV DOTNET_SDK_VERSION 1.0.0-preview2-1-003177  
ENV DOTNET_SDK_DOWNLOAD_URL
https://dotnetcli.blob.core.windows.net/dotnet/preview/Binaries/$DOTNET_SDK_VERSION/dotnet-
dev-debian-x64.$DOTNET_SDK_VERSION.tar.gz  
  
RUN curl -SL $DOTNET_SDK_DOWNLOAD_URL \--output dotnet.tar.gz \  
&& mkdir -p /usr/share/dotnet \  
&& tar -zxf dotnet.tar.gz -C /usr/share/dotnet \  
&& rm dotnet.tar.gz \  
&& ln -s /usr/share/dotnet/dotnet /usr/bin/dotnet  
  
# Trigger the population of the local package cache  
ENV NUGET_XMLDOC_MODE skip  
RUN mkdir warmup \  
&& cd warmup \  
&& cd .. \  
&& rm -rf warmup \  
&& rm -rf /tmp/NuGetScratch  
#  
RUN apt-get update  
RUN apt-get install -yq sudo  
  
RUN npm install -g yo bower generator-aspnet  
RUN adduser --disabled-password --gecos "" yeoman; \  
echo "yeoman ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
RUN mkdir /src && chown -R yeoman:yeoman /src  
USER yeoman  
  
EXPOSE 5000  
VOLUME /src  
WORKDIR /src  
#-d modunda calısabilsin diye  
CMD ['/bin/bash']

