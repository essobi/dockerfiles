FROM vixns/jenkins-dind  
USER root  
RUN curl -fsSL get.docker.com -o get-docker.sh && \  
sh get-docker.sh && \  
service docker start && \  
apt-get update && \  
apt-get -y install curl libunwind8 gettext apt-transport-https && \  
curl https://packages.microsoft.com/keys/microsoft.asc | gpg \--dearmor >
microsoft.gpg && \  
mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg && \  
sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-
debian-stretch-prod stretch main" > /etc/apt/sources.list.d/dotnetdev.list' &&
\  
apt-get update && \  
apt-get -y install dotnet-sdk-2.1.4 && \  
export PATH=$PATH:$HOME/dotnet  

