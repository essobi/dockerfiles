FROM ubuntu:xenial  
  
# Install .NET Core  
ENV DOTNET_VERSION 1.1.1  
ENV DOTNET_DOWNLOAD_URL
https://dotnetcli.blob.core.windows.net/dotnet/release/1.1.0/Binaries/$DOTNET_VERSION/dotnet-
debian-x64.$DOTNET_VERSION.tar.gz  
  
# Setup the locale  
ENV LANG en_US.UTF-8  
ENV LC_ALL $LANG  
ENV LANGUAGE $LANG  
  
# Install dependencies and clean up  
RUN echo 'deb http://security.ubuntu.com/ubuntu trusty-security main' >>
/etc/apt/sources.list \  
&& echo 'deb http://archive.ubuntu.com/ubuntu/ trusty-updates main' >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
# PowerShell dependencies  
apt-utils \  
ca-certificates \  
curl \  
apt-transport-https \  
\  
# .NET core dependencies  
ca-certificates \  
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
\  
# Java  
openjdk-8-jre \  
# misc stuff  
liblldb-3.6 \  
locales \  
ant \  
&& locale-gen $LANG \  
&& update-locale  
  
# Import the public repository GPG keys for Microsoft  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \  
# Register the Microsoft Ubuntu 16.04 repository  
&& curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list | tee
/etc/apt/sources.list.d/microsoft.list \  
# Install powershell from Microsoft Repo  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
powershell \  
&& rm -rf /var/lib/apt/lists/* \  
# Install dotnetcore  
&& curl -SL $DOTNET_DOWNLOAD_URL --output dotnet.tar.gz \  
&& mkdir -p /usr/share/dotnet \  
&& tar -zxf dotnet.tar.gz -C /usr/share/dotnet \  
&& rm dotnet.tar.gz \  
&& ln -s /usr/share/dotnet/dotnet /usr/bin/dotnet  
  
# Use array to avoid Docker prepending /bin/sh -c  
ENTRYPOINT [ "powershell" ]  

