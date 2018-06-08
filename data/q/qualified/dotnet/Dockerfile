FROM microsoft/dotnet:2.0.0-sdk-stretch  
  
RUN set -ex; \  
useradd --create-home codewarrior; \  
ln -s /home/codewarrior /workspace;  
  
RUN set -ex; \  
apt-get update; \  
apt-get install -y --no-install-recommends \  
xsltproc \  
; \  
rm -rf /var/lib/apt/lists/*;  
  
COPY rootfs/runner /runner  
COPY rootfs/workspace /workspace  
  
RUN set -ex; \  
# chown -R codewarrior:codewarrior /runner/qualified-event-listener; \  
chown -R codewarrior:codewarrior /home/codewarrior;  
  
USER codewarrior  
ENV USER=codewarrior \  
HOME=/home/codewarrior \  
DOTNET_CLI_TELEMETRY_OPTOUT=1  
RUN set -ex; \  
# cd /runner/qualified-event-listener; dotnet restore; \  
cd /workspace/cs-run; dotnet restore; \  
cd /workspace/cs-test; dotnet restore; \  
cd /workspace/fs-run; dotnet restore;  
  
WORKDIR /workspace  

