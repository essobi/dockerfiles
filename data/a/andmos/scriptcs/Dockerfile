FROM mono:latest  
  
RUN \  
apt-get update && \  
apt-get install -y && \  
apt-get install -y git && \  
mkdir /opt/workdir && \  
cd /opt/workdir/ && \  
git clone https://github.com/scriptcs/scriptcs && \  
cd scriptcs && \  
git checkout master  
  
WORKDIR /opt/workdir/scriptcs/  
  
RUN nuget restore ./ScriptCs.sln  
RUN mkdir artifacts --parents  
RUN xbuild ./ScriptCs.sln /property:Configuration=Release /nologo
/verbosity:normal  
RUN mono ./packages/xunit.runners.1.9.2/tools/xunit.console.clr4.exe
test/ScriptCs.Tests.Acceptance/bin/Release/ScriptCs.Tests.Acceptance.dll  
  
RUN apt-get clean  
  
ENTRYPOINT ["mono",
"/opt/workdir/scriptcs/src/ScriptCs/bin/Release/scriptcs.exe"]  

