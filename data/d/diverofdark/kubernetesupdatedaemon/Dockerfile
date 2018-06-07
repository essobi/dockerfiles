FROM microsoft/dotnet:2.0.4-sdk-2.1.3 as builder  
COPY . /build  
WORKDIR /build  
  
RUN dotnet restore  
RUN dotnet publish --output ../out/ --configuration Release KubeUpdateDaemon  
  
FROM microsoft/dotnet:2.0.4-runtime  
  
RUN apt-get update -y && \  
apt-get install -y --no-install-recommends dirmngr \  
htop \  
ca-certificates \  
wget \  
apt-transport-https gnupg2 \  
apt-utils \  
lsb-release \  
sudo \  
nano && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN echo "deb [arch=amd64] https://download.docker.com/linux/debian jessie
stable" > /etc/apt/sources.list.d/docker.list && \  
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -  
  
RUN apt-get update -y && \  
apt-get install -y \  
docker-ce && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /app  
COPY \--from=builder /build/out .  
  
ADD kubectl .  
ADD entrypoint .  
  
RUN chmod +x kubectl && chmod +x entrypoint  
  
ENTRYPOINT ["/app/entrypoint"]  

