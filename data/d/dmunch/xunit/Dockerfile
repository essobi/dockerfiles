FROM dmunch/mono  
  
# Install NuGet  
RUN mkdir -p /usr/local/share/mono/  
WORKDIR /usr/local/share/mono/  
RUN wget 'https://github.com/NuGet/Home/releases/download/3.2/nuget.exe' -O
NuGet.exe  
  
RUN mono NuGet.exe update -self  
RUN mono NuGet.exe install xunit  
RUN mono NuGet.exe install xunit.extensions  
RUN mono NuGet.exe install  
  
RUN mono NuGet.exe install xunit.runner.console  
  
WORKDIR /src  
  
#would be better to create an alias  
RUN echo "mono
/usr/local/share/mono/xunit.runner.console.2.1.0/tools/xunit.console.x86.exe
\$1" > /usr/local/bin/xunit  
RUN chmod +x /usr/local/bin/xunit  

