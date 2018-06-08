FROM buildpack-deps:xenial  
  
RUN set -ex; \  
useradd --create-home codewarrior; \  
ln -s /home/codewarrior /workspace;  
  
# Installing binary archives to lock the version  
#
https://github.com/PowerShell/PowerShell/blob/master/docs/installation/linux.md#binary-
archives  
RUN set -ex; \  
apt-get update; \  
apt-get install -y --no-install-recommends \  
libc6 \  
libgcc1 \  
libgssapi-krb5-2 \  
liblttng-ust0 \  
libstdc++6 \  
libcurl3 \  
libunwind8 \  
libuuid1 \  
zlib1g \  
libssl1.0.0 \  
libicu55 \  
; \  
rm -rf /var/lib/apt/lists/*; \  
\  
curl -L -o /tmp/powershell.tar.gz
https://github.com/PowerShell/PowerShell/releases/download/v6.0.0/powershell-6.0.0-linux-x64.tar.gz;
\  
mkdir -p /opt/microsoft/powershell/6.0.0; \  
tar zxf /tmp/powershell.tar.gz -C /opt/microsoft/powershell/6.0.0; \  
rm /tmp/powershell.tar.gz; \  
chmod +x /opt/microsoft/powershell/6.0.0/pwsh; \  
ln -s /opt/microsoft/powershell/6.0.0/pwsh /usr/bin/pwsh; \  
rm /opt/microsoft/powershell/6.0.0/DELETE_ME_TO_DISABLE_CONSOLEHOST_TELEMETRY;  
  
# Install Pester 4.1.1  
# /usr/local/share/powershell/Modules/Pester  
RUN set -ex; \  
pwsh -Command Set-PSRepository -Name PSGallery -InstallationPolicy Trusted; \  
pwsh -Command Install-Module -Name Pester -RequiredVersion 4.1.1;  
  
COPY rootfs/runner /runner  
  
USER codewarrior  
ENV USER=codewarrior \  
HOME=/home/codewarrior  
WORKDIR /workspace  

