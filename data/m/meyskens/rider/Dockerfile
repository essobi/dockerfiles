FROM meyskens/desktop-base  
  
RUN wget
https://download.jetbrains.com/resharper/JetBrains.Rider-2017.1.tar.gz &&\  
tar -xzf JetBrains.Rider-2017.1.tar.gz  
  
RUN echo "deb http://ftp.de.debian.org/debian/ jessie main"
>>/etc/apt/sources.list  
  
# Add .net core  
RUN apt-get update &&\  
apt-get install -y --no-install-recommends \  
libc6 \  
libcurl3 \  
libgcc1 \  
libgssapi-krb5-2 \  
liblttng-ust0 \  
libstdc++6 \  
libunwind8 \  
libuuid1 \  
zlib1g \  
curl &&\  
apt-get -t jessie -y install libicu52 libssl1.0.0 &&\  
rm -rf /var/lib/apt/lists/*  
  
# Install .NET Core SDK  
ENV DOTNET_SDK_VERSION 1.0.4  
ENV DOTNET_SDK_DOWNLOAD_URL
https://dotnetcli.blob.core.windows.net/dotnet/Sdk/$DOTNET_SDK_VERSION/dotnet-
dev-debian-x64.$DOTNET_SDK_VERSION.tar.gz  
  
RUN curl -SL $DOTNET_SDK_DOWNLOAD_URL \--output dotnet.tar.gz \  
&& mkdir -p /usr/share/dotnet \  
&& tar -zxf dotnet.tar.gz -C /usr/share/dotnet \  
&& rm dotnet.tar.gz \  
&& ln -s /usr/share/dotnet/dotnet /usr/bin/dotnet  
  
CMD Rider-2017.1/bin/rider.sh

