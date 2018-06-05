FROM travix/gocd-agent-gcloud:18.5.0  
  
MAINTAINER Travix  
  
# Work around https://github.com/dotnet/cli/issues/1582 until Docker releases
a  
# fix (https://github.com/docker/docker/issues/20818). This workaround allows  
# the container to be run with the default seccomp Docker settings by avoiding  
# the restart_syscall made by LTTng which causes a failed assertion.  
ENV LTTNG_UST_REGISTER_TIMEOUT 0  
ENV DOTNET_CLI_TELEMETRY_OPTOUT 1  
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
ca-certificates \  
curl \  
gettext \  
nuget \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install .NET Core  
# We're installing both 1.0.1 and 1.1.0. After all applications are updated,
1.0.1 can be removed.  
# .NET Core 1.0.1  
RUN curl -sSL -o dotnet.tar.gz https://go.microsoft.com/fwlink/?LinkID=827530
\  
&& mkdir -p /opt/dotnet \  
&& tar zxf dotnet.tar.gz -C /opt/dotnet \  
&& rm -rf dotnet.tar.gz  
  
# .NET Core 1.1.0  
RUN curl -sSL -o dotnet.tar.gz https://go.microsoft.com/fwlink/?LinkID=835021
\  
&& mkdir -p /opt/dotnet \  
&& tar zxf dotnet.tar.gz -C /opt/dotnet \  
&& rm -rf dotnet.tar.gz  
  
# .NET Core 1.1.1  
RUN curl -sSL -o dotnet.tar.gz https://go.microsoft.com/fwlink/?linkid=843453
\  
&& mkdir -p /opt/dotnet \  
&& tar zxf dotnet.tar.gz -C /opt/dotnet \  
&& rm -rf dotnet.tar.gz \  
&& ln -s /opt/dotnet/dotnet /usr/bin  
  
# Trigger the population of the local package cache  
ENV NUGET_XMLDOC_MODE skip  
RUN mkdir warmup \  
&& cd warmup \  
&& dotnet new \  
&& cd .. \  
&& rm -rf warmup \  
&& rm -rf /tmp/NuGetScratch  
  
# fix nuget push issue (http://stackoverflow.com/questions/15181888/nuget-on-
linux-error-getting-response-stream)  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \  
&& echo "deb http://download.mono-project.com/repo/debian wheezy main" | tee
/etc/apt/sources.list.d/mono-xamarin.list \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates-mono \  
mono-complete \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

