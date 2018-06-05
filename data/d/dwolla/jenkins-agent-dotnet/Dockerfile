FROM openjdk:8-jre  
MAINTAINER Dwolla Dev <dev+jenkins-dotnet@dwolla.com>  
LABEL org.label-schema.vcs-url="https://github.com/Dwolla/jenkins-agent-
docker-dotnet"  
  
ENV JENKINS_HOME=/home/jenkins \  
JENKINS_AGENT=/usr/share/jenkins \  
AGENT_VERSION=2.61  
COPY jenkins-agent /usr/local/bin/jenkins-agent  
  
RUN apt-get update && apt-get install -y --no-install-recommends git  
ENV DOTNET_CLI_TELEMETRY_OPTOUT 1  
ENV DOTNET_SKIP_FIRST_TIME_EXPERIENCE 1  
### Start .NET, from https://github.com/dotnet/dotnet-
docker/blob/master/2.0/sdk/stretch/amd64/Dockerfile  
# Install .NET CLI dependencies  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libc6 \  
libcurl3 \  
libgcc1 \  
libgssapi-krb5-2 \  
libicu57 \  
liblttng-ust0 \  
libssl1.0.2 \  
libstdc++6 \  
libunwind8 \  
libuuid1 \  
zlib1g \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install .NET Core SDK  
ENV DOTNET_SDK_VERSION 2.0.0  
ENV DOTNET_SDK_DOWNLOAD_URL
https://dotnetcli.blob.core.windows.net/dotnet/Sdk/$DOTNET_SDK_VERSION/dotnet-
sdk-$DOTNET_SDK_VERSION-linux-x64.tar.gz  
ENV DOTNET_SDK_DOWNLOAD_SHA
E457F3A5685382F7F24851A2E76EDBE75B575948C8A7F43220F159BA29C329A5008BBE7220C18DFB31EAF0398FC72177B1948B65E19B34ED0D907EFB459CF4B0  
  
RUN curl -SL $DOTNET_SDK_DOWNLOAD_URL \--output dotnet.tar.gz \  
&& echo "$DOTNET_SDK_DOWNLOAD_SHA dotnet.tar.gz" | sha512sum -c - \  
&& mkdir -p /usr/share/dotnet \  
&& tar -zxf dotnet.tar.gz -C /usr/share/dotnet \  
&& rm dotnet.tar.gz \  
&& ln -s /usr/share/dotnet/dotnet /usr/bin/dotnet  
  
# Trigger the population of the local package cache  
ENV NUGET_XMLDOC_MODE skip  
RUN mkdir warmup \  
&& cd warmup \  
&& dotnet new \  
&& cd .. \  
&& rm -rf warmup \  
&& rm -rf /tmp/NuGetScratch  
### END .NET  
RUN curl --create-dirs -sSLo ${JENKINS_AGENT}/agent.jar https://repo.jenkins-
ci.org/public/org/jenkins-
ci/main/remoting/${AGENT_VERSION}/remoting-${AGENT_VERSION}.jar && \  
chmod 755 ${JENKINS_AGENT} && \  
chmod 644 ${JENKINS_AGENT}/agent.jar && \  
mkdir -p ${JENKINS_HOME} && \  
useradd --home ${JENKINS_HOME} \--system jenkins && \  
chown -R jenkins ${JENKINS_HOME} && \  
chmod 755 /usr/local/bin/jenkins-agent && \  
apt-get clean  
  
WORKDIR ${JENKINS_HOME}  
USER jenkins  
  
RUN git config --global user.email "dev+jenkins@dwolla.com" && \  
git config --global user.name "Jenkins Build Agent"  
  
ENTRYPOINT ["jenkins-agent"]  

