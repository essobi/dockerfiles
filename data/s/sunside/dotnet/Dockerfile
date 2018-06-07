FROM sunside/xenial-mono:5.3.0.67  
MAINTAINER Markus Mayer <awesome@nyris.io>  
  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor >
microsoft.gpg \  
&& mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg \  
&& apt-get update \  
&& apt-get install -y apt-transport-https \  
&& sh -c 'echo "deb [arch=amd64]
https://packages.microsoft.com/repos/microsoft-ubuntu-xenial-prod xenial main"
> /etc/apt/sources.list.d/dotnetdev.list' \  
&& apt-get update \  
&& apt-get install -y dotnet-sdk-2.1.4 \  
&& apt-get -y autoremove \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN wget -O /tmp/dotnet-1.1.7.tgz -c
https://download.microsoft.com/download/4/E/6/4E64A465-F02E-43AD-9A86-A08A223A82C3/dotnet-
dev-ubuntu.16.04-x64.1.1.7.tar.gz \  
&& tar --skip-old-files -xzvf /tmp/dotnet-1.1.7.tgz -C /usr/share/dotnet/ \  
&& rm /tmp/dotnet-1.1.7.tgz  
  
# Workaround for https://github.com/dotnet/cli/issues/1582, Bug only appears
in Docker < 1.11.0  
ENV LTTNG_UST_REGISTER_TIMEOUT 0  
# fix for System.Native not being found on net4xx targets  
ENV SYSTEM_NATIVE_DLL
/usr/share/dotnet/shared/Microsoft.NETCore.App/2.0.5/System.Native.so  
RUN test -e ${SYSTEM_NATIVE_DLL} && \  
ln -s ${SYSTEM_NATIVE_DLL} /usr/lib/libSystem.Native.so && \  
ldconfig  
  
# Trigger the population of the local package cache  
ENV NUGET_XMLDOC_MODE skip  
RUN mkdir warmup \  
&& cd warmup \  
&& dotnet new \  
&& cd .. \  
&& rm -rf warmup  
  
# Workaround to build and run netXXX apps using dotnet  
ENV FrameworkPathOverride /usr/lib/mono/4.5/  

