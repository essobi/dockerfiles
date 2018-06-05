FROM mono  
  
ENV RHOST="rserve"  
MAINTAINER "Bas van Reeuwijk" bvk@qlik.com  
  
# Details  
LABEL version="1.0"  
LABEL description="Image running SSEtoRserve in mono"  
  
# Initial setup  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install git unzip supervisor -y  
  
# Get SSEtoRserve sources  
RUN git clone https://github.com/wbvreeuwijk/sse-r-plugin.git  
  
# Setup build environment  
WORKDIR /sse-r-plugin/csharp  
RUN nuget restore \  
&& temp_dir=packages/Grpc.Tools.1.4.x/tmp \  
&& curl_url=https://www.nuget.org/api/v2/package/Grpc.Tools/ \  
&& mkdir -p $temp_dir \  
&& cd $temp_dir \  
&& curl -sL $curl_url > tmp.zip; unzip tmp.zip \  
&& cd .. \  
&& cp -r tmp/tools . \  
&& rm -rf tmp \  
&& cd ../.. \  
&& chmod 755 packages/Grpc.Tools.1.4.x/tools/linux_x64/protoc \  
&& chmod 755 packages/Grpc.Tools.1.4.x/tools/linux_x64/grpc_csharp_plugin \  
&& chmod 755 ServerSideExtension/generate_SSE_Stubs_from_proto.sh  
  
# Build application  
RUN msbuild ServerSideExtension.sln  
  
# Cleanup  
RUN rm -rf ServerSideExtension packages  
  
# Port SSEtoRserve is going to listen on  
EXPOSE ${PORT:-50051}  
  
# Create configuration file for SSEtoRserve  
RUN { \  
echo '<?xml version="1.0" encoding="utf-8" ?>';\  
echo ' <configuration>';\  
echo ' <configSections>';\  
echo ' <sectionGroup name="applicationSettings"
type="System.Configuration.ApplicationSettingsGroup, System, Version=4.0.0.0,
Culture=neutral, PublicKeyToken=b77a5c561934e089" >';\  
echo ' <section name="SSEtoRserve.Properties.Settings"
type="System.Configuration.ClientSettingsSection, System, Version=4.0.0.0,
Culture=neutral, PublicKeyToken=b77a5c561934e089" requirePermission="false"
/>';\  
echo ' </sectionGroup>';\  
echo ' </configSections>';\  
echo ' <startup>';\  
echo ' <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.5.2"
/>';\  
echo ' </startup>';\  
echo ' <applicationSettings>';\  
echo ' <SSEtoRserve.Properties.Settings>';\  
echo ' <setting name="grpcPort" serializeAs="String">';\  
echo ' <value>50051</value>';\  
echo ' </setting>';\  
echo ' <setting name="rserveHost" serializeAs="String">';\  
echo ' <value>$rServeHost</value>';\  
echo ' </setting>';\  
echo ' <setting name="rservePort" serializeAs="String">';\  
echo ' <value>6311</value>';\  
echo ' </setting>';\  
echo ' <setting name="grpcHost" serializeAs="String">';\  
echo ' <value>0.0.0.0</value> <!-- Set to 0.0.0.0 if you want it reachable
from the outside world -->';\  
echo ' </setting>';\  
echo ' </SSEtoRserve.Properties.Settings>';\  
echo ' </applicationSettings>';\  
echo '</configuration>';\  
} | tee /sse-r-plugin/csharp/SSEtoRserve/bin/Debug/SSEtoRserve.exe.tmpl  
  
# Create start script  
RUN { \  
echo "#!/bin/sh";\  
echo "export IPADDR=\\`getent hosts \$RHOST | awk '{ print \$1 ; exit }'\\`";\  
echo "export IPADDR=\${IPADDR:-127.0.0.1}";\  
echo "sed 's/\$rServeHost/'\$IPADDR'/' /sse-r-
plugin/csharp/SSEtoRserve/bin/Debug/SSEtoRserve.exe.tmpl > /sse-r-
plugin/csharp/SSEtoRserve/bin/Debug/SSEtoRserve.exe.config";\  
echo "/usr/bin/mono /sse-r-
plugin/csharp/SSEtoRserve/bin/Debug/SSEtoRserve.exe";\  
} | tee /sse-r-plugin/csharp/start.sh  
RUN chmod 755 /sse-r-plugin/csharp/start.sh  
  
# Start command  
ENTRYPOINT ["/bin/sh", "-c", "/sse-r-plugin/csharp/start.sh"]

