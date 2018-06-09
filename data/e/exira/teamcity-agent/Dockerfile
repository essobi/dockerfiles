FROM java:8-jre  
MAINTAINER Alexander Gorokhov <sashgorokhov@gmail.com>  
  
RUN apt-get update && apt-get install -y unzip git  
  
ENV SERVER_URL="" \  
AGENT_OWN_ADDRESS="" \  
AGENT_OWN_PORT="9090" \  
AGENT_NAME="" \  
AGENT_DIR="/opt/teamcity_agent"  
  
ENV AGENT_WORKDIR=$AGENT_DIR"/work_dir" \  
AGENT_TEMPDIR=$AGENT_DIR"/temp_dir"  
  
EXPOSE $AGENT_OWN_PORT  
VOLUME $AGENT_WORKDIR $AGENT_TEMPDIR  
WORKDIR $AGENT_DIR  
  
COPY setup_agent.sh /  
  
RUN \  
# Install docker  
wget -P /tmp https://get.docker.com/builds/Linux/x86_64/docker-1.11.2.tgz && \  
tar -xzf /tmp/docker-1.11.2.tgz -C / && rm /tmp/docker-1.11.2.tgz && \  
ln -s /docker/docker /usr/local/bin/docker && \  
  
# Install Mono  
#apt-get update && apt-get install -y mono-complete && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \  
echo "deb http://download.mono-project.com/repo/debian wheezy main" | tee
/etc/apt/sources.list.d/mono-xamarin.list && \  
echo "deb http://download.mono-project.com/repo/debian wheezy-apache24-compat
main" | tee -a /etc/apt/sources.list.d/mono-xamarin.list && \  
echo "deb http://download.mono-project.com/repo/debian wheezy-libjpeg62-compat
main" | tee -a /etc/apt/sources.list.d/mono-xamarin.list && \  
apt-get clean && \  
apt-get update && \  
apt-get install -f -y mono-devel mono-complete referenceassemblies-pcl ca-
certificates-mono && \  
  
# Install F#  
apt-get clean && \  
apt-get update && \  
apt-get install -y fsharp && \  
  
# Install .NET Core  
apt-get clean && \  
apt-get update && \  
apt-get install -y curl libunwind8 gettext && \  
curl -sSL -o dotnet.tar.gz https://go.microsoft.com/fwlink/?LinkID=835021 && \  
mkdir -p /opt/dotnet && tar zxf dotnet.tar.gz -C /opt/dotnet && \  
ln -s /opt/dotnet/dotnet /usr/local/bin && \  
  
# Install Node, NPM and Octopus Helpers  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get clean && \  
apt-get update && \  
apt-get install -y nodejs && \  
npm install bower octopus-deploy -g  
  
CMD /setup_agent.sh && $AGENT_DIR/bin/agent.sh run  

