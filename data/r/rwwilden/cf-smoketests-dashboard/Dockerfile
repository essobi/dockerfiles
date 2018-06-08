FROM codesimple/elm:0.18  
LABEL maintainer="Ronald Wildenberg"  
  
ENV DOTNET_SDK_VERSION "2.1.3"  
ENV DOTNET_CLI_TELEMETRY_OPTOUT 1  
ENV DOTNET_SKIP_FIRST_TIME_EXPERIENCE 1  
ENV CF_CLI_VERSION "6.32.0"  
# https://docs.microsoft.com/en-us/dotnet/core/linux-
prerequisites?tabs=netcore2x#install-net-core-for-debian-8-or-debian-9-64-bit  
RUN apt-get update &&\  
apt-get install -y curl libunwind8 gettext apt-transport-https &&\  
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor >
microsoft.gpg &&\  
mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg &&\  
sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-
debian-jessie-prod jessie main" > /etc/apt/sources.list.d/dotnetdev.list' &&\  
apt-get update &&\  
apt-get install -y dotnet-sdk-$DOTNET_SDK_VERSION  
  
# Install CF CLI  
RUN curl -L
"https://cli.run.pivotal.io/stable?release=linux64-binary&version=${CF_CLI_VERSION}"
| tar -xz -C /usr/local/bin  
  

