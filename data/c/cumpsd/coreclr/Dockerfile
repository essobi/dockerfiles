FROM ubuntu:trusty  
  
MAINTAINER exira.com <info@exira.com>  
  
# Latest known good for F#  
ENV DOTNET_VERSION=1.0.0-beta-002071 \  
MSBUILD_VERSION=0.1.0-preview-00022  
# Latest from docs  
#ENV DOTNET_VERSION=1.0.0.001598-1 \  
# MSBUILD_VERSION=0.1.0-preview-00022  
# Latest from Github  
#ENV DOTNET_VERSION=1.0.0-rc2-002468 \  
# MSBUILD_VERSION=0.1.0-preview-00022  
# Work around https://github.com/dotnet/cli/issues/1582 until Docker releases
a  
# fix (https://github.com/docker/docker/issues/20818). This workaround allows  
# the container to be run with the default seccomp Docker settings by avoiding  
# the restart_syscall made by LTTng which causes a failed assertion.  
ENV LTTNG_UST_REGISTER_TIMEOUT 0  
  
RUN echo "deb [arch=amd64] http://apt-mo.trafficmanager.net/repos/dotnet/
trusty main" > /etc/apt/sources.list.d/dotnetdev.list && \  
apt-key adv --keyserver apt-mo.trafficmanager.net --recv-keys 417A0893 && \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
#dotnet=${DOTNET_VERSION} \  
dotnet-dev-${DOTNET_VERSION} \  
dotnet-host=${DOTNET_VERSION}-1 \  
ca-certificates \  
wget \  
unzip \  
nano \  
git && \  
  
wget -P /tmp/MSBuild https://www.myget.org/F/dotnet-
buildtools/api/v2/package/MSBuild/${MSBUILD_VERSION} && \  
wget -P /tmp/Microsoft.Build https://www.myget.org/F/dotnet-
buildtools/api/v2/package/Microsoft.Build/${MSBUILD_VERSION} && \  
wget -P /tmp/Microsoft.Build.Framework https://www.myget.org/F/dotnet-
buildtools/api/v2/package/Microsoft.Build.Framework/${MSBUILD_VERSION} && \  
wget -P /tmp/Microsoft.Build.Tasks.Core https://www.myget.org/F/dotnet-
buildtools/api/v2/package/Microsoft.Build.Tasks.Core/${MSBUILD_VERSION} && \  
wget -P /tmp/Microsoft.Build.Utilities.Core https://www.myget.org/F/dotnet-
buildtools/api/v2/package/Microsoft.Build.Utilities.Core/${MSBUILD_VERSION} &&
\  
wget -P /tmp/Microsoft.Build.Targets https://www.myget.org/F/dotnet-
buildtools/api/v2/package/Microsoft.Build.Targets/${MSBUILD_VERSION} && \  
  
unzip -jo /tmp/MSBuild/${MSBUILD_VERSION} runtimes/any/native/MSBuild.exe -d
/usr/share/dotnet/msbuild/ && \  
unzip -jo /tmp/Microsoft.Build/${MSBUILD_VERSION}
lib/dotnet/Microsoft.Build.dll -d /usr/share/dotnet/msbuild/ && \  
unzip -jo /tmp/Microsoft.Build.Framework/${MSBUILD_VERSION}
lib/dotnet/Microsoft.Build.Framework.dll -d /usr/share/dotnet/msbuild/ && \  
unzip -jo /tmp/Microsoft.Build.Tasks.Core/${MSBUILD_VERSION}
lib/dotnet/Microsoft.Build.Tasks.Core.dll -d /usr/share/dotnet/msbuild/ && \  
unzip -jo /tmp/Microsoft.Build.Utilities.Core/${MSBUILD_VERSION}
lib/dotnet/Microsoft.Build.Utilities.Core.dll -d /usr/share/dotnet/msbuild/ &&
\  
unzip -jo /tmp/Microsoft.Build.Targets/${MSBUILD_VERSION} -d
/usr/share/dotnet/msbuild/Microsoft.Build.Targets && \  
  
ln -s /usr/share/dotnet/shared/Microsoft.NETCore.App/1.0.0-rc2-23925
/usr/share/dotnet/shared/Microsoft.NETCore.App/1.0.0-rc2-23929 && \  
  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
ENV PATH=/usr/share/dotnet:/usr/share/dotnet/sdk/${DOTNET_VERSION}:$PATH \  
LANG=en_US.UTF-8  
  
COPY fsc fsi /usr/share/dotnet/sdk/${DOTNET_VERSION}/  
COPY msbuild /usr/share/dotnet/msbuild/  
  
RUN chmod +x /usr/share/dotnet/sdk/${DOTNET_VERSION}/fsc && \  
chmod +x /usr/share/dotnet/sdk/${DOTNET_VERSION}/fsi && \  
chmod +x /usr/share/dotnet/msbuild/msbuild  

