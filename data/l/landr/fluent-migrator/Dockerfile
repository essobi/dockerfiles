#  
# Start from an image that includes the mssql-tools. This is based on ubuntu
16.04  
#  
FROM microsoft/mssql-tools  
  
# Install a basic version of Mono and related tools.  
# This was inspired by the following Dockerfiles  
#  
#
https://github.com/mono/docker/blob/c05f965729b45093c1e9534d3e6532984f8091db/5.4.1.6/slim/Dockerfile  
#
https://github.com/mono/docker/blob/c05f965729b45093c1e9534d3e6532984f8091db/5.4.1.6/Dockerfile  
#  
ENV MONO_VERSION 5.4.1.6  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF  
  
RUN echo "deb http://download.mono-project.com/repo/debian
jessie/snapshots/$MONO_VERSION main" > /etc/apt/sources.list.d/mono-
official.list \  
&& apt-get update \  
&& apt-get install -y mono-runtime binutils curl mono-devel nuget unzip \  
&& rm -rf /var/lib/apt/lists/* /tmp/*  
  
#  
# Install FluentMigrator.Tools  
#  
RUN mkdir /tmp/FluentMigrator.Tools \  
&& nuget install FluentMigrator.Tools -Version 1.6.2 -OutputDirectory
/tmp/FluentMigrator.Tools/ \  
&& mv /tmp/FluentMigrator.Tools/FluentMigrator.Tools.1.6.2/tools
/usr/local/bin/FluentMigrator.Tools \  
&& rm -rf /tmp/FluentMigrator.Tools  
  
ADD UpgradeDatabase.sh /usr/local/bin/UpgradeDatabase.sh  
ENTRYPOINT ["UpgradeDatabase.sh"]

