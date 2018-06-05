  
FROM microsoft/dotnet:2-sdk  
LABEL Name=ncig.docker.cakebuild Version=1.0.0  
  
# Set timezone  
RUN ln -sf /usr/share/zoneinfo/Australia/Sydney /etc/localtime  
  
# Install node  
RUN apt-get update  
RUN apt-get install -y curl  
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash -  
RUN apt-get install -y nodejs  
  
# Install mono - pinned to v4.8.0, see http://www.mono-
project.com/docs/getting-started/install/linux/#accessing-older-releases  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF  
RUN echo "deb http://download.mono-project.com/repo/debian
wheezy/snapshots/4.8.0 main" | tee /etc/apt/sources.list.d/mono-official.list  
RUN apt-get update  
RUN apt-get install -y mono-devel  
  
# Install libgit, required by GitVersion. Note that additional configuration
is required  
# to point GitVersion at this library, this is done in the build.cake script  
# after GitVersion installation.  
RUN apt-get install -y libgit2-24  
RUN ln -s /usr/lib/x86_64-linux-gnu/libgit2.so.24 /usr/lib/x86_64-linux-
gnu/libgit2.so  
  
# Install jq - used to interpret results of Bitbucket API calls  
RUN apt-get install -y jq  
  
# Install chromium for headless browser testing in Karma.  
RUN apt-get install -y chromium  
  
# Install zip for AWS packaging.  
RUN apt-get install -y zip  

