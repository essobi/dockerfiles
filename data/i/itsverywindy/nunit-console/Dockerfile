FROM mono:4.0.1  
  
ENV NUNIT_VERSION 2.6.4  
  
RUN \  
apt-get update && \  
apt-get install -y && \  
apt-get install -y wget && \  
nuget install NUnit.Runners -o /tmp/nunit -version $NUNIT_VERSION && \  
mkdir /nunit && \  
cp /tmp/nunit/NUnit.Runners.$NUNIT_VERSION/tools/nunit-console.exe /nunit && \  
cp /tmp/nunit/NUnit.Runners.$NUNIT_VERSION/tools/nunit-console.exe.config
/nunit && \  
cp /tmp/nunit/NUnit.Runners.$NUNIT_VERSION/tools/nunit.framework.dll /nunit &&
\  
cp /tmp/nunit/NUnit.Runners.$NUNIT_VERSION/tools/lib/nunit-console-runner.dll
/nunit && \  
cp /tmp/nunit/NUnit.Runners.$NUNIT_VERSION/tools/lib/nunit.util.dll /nunit &&
\  
cp /tmp/nunit/NUnit.Runners.$NUNIT_VERSION/tools/lib/nunit.core.interfaces.dll
/nunit && \  
cp /tmp/nunit/NUnit.Runners.$NUNIT_VERSION/tools/lib/nunit.core.dll /nunit &&
\  
  
apt-get clean  
  
ENTRYPOINT ["mono", "/nunit/nunit-console.exe"]

