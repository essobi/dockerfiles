FROM mono:latest  
  
MAINTAINER gabrielaraujof <contact@gbiel.com>  
  
ENV NUNIT_VERSION 3.5.0  
  
RUN \  
apt-get update && \  
apt-get install -y && \  
apt-get install -y wget && \  
nuget install NUnit.Runners -o /tmp/nunit -version $NUNIT_VERSION && \  
ls /tmp/nunit && \  
mkdir /nunit && \  
cp /tmp/nunit/NUnit.ConsoleRunner.$NUNIT_VERSION/tools/* /nunit && \  
cp /tmp/nunit/NUnit.Extension.NUnitProjectLoader.$NUNIT_VERSION/tools/* /nunit
&& \  
cp /tmp/nunit/NUnit.Extension.NUnitV2Driver.$NUNIT_VERSION/tools/* /nunit && \  
cp /tmp/nunit/NUnit.Extension.NUnitV2ResultWriter.$NUNIT_VERSION/tools/*
/nunit && \  
cp /tmp/nunit/NUnit.Extension.VSProjectLoader.$NUNIT_VERSION/tools/* /nunit &&
\  
apt-get clean  
  
ENTRYPOINT ["mono", "/nunit/nunit3-console.exe"]  

