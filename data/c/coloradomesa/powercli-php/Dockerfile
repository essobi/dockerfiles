FROM php:apache  
# install packages  
ARG POWERSHELL_RELEASE=v6.0.0-alpha.18  
ARG POWERSHELL_PACKAGE=powershell_6.0.0-alpha.18-1ubuntu1.16.04.1_amd64.deb  
ARG POWERCLI_PACKAGE=PowerCLI.ViCore.zip  
ARG POWERCLI_VDS_PACKAGE=PowerCLI.Vds.zip  
  
RUN echo "deb http://ftp.de.debian.org/debian sid main" >>
/etc/apt/sources.list && apt-get update  
  
RUN apt-get update && \  
apt-get install --no-install-recommends -yq \  
openssh-server \  
ca-certificates \  
curl \  
libunwind8 \  
libicu57 \  
unzip \  
wget \  
libcurl4-openssl-dev \  
git  
  
# Forcibly install libicu55  
RUN curl -SLO
http://archive.ubuntu.com/ubuntu/pool/main/i/icu/libicu55_55.1-7_amd64.deb \  
&& dpkg -i libicu55_55.1-7_amd64.deb \  
&& rm libicu55_55.1-7_amd64.deb  
  
# Create new user and set working directory to /home/powershell  
RUN useradd -ms /usr/bin/powershell powershell  
WORKDIR /home/powershell  
  
# Install PowerShell package and clean up  
RUN curl -SLO
https://github.com/PowerShell/PowerShell/releases/download/$POWERSHELL_RELEASE/$POWERSHELL_PACKAGE
\  
&& dpkg -i $POWERSHELL_PACKAGE \  
&& rm $POWERSHELL_PACKAGE  
  
#Use powershell user going forward  
USER powershell  
  
# Download and Unzip the PowerCLI module to the users module directory  
RUN wget https://download3.vmware.com/software/vmw-
tools/powerclicore/PowerCLI_Core.zip  
RUN ls -la && pwd && unzip PowerCLI_Core.zip -d /home/powershell/  
RUN mkdir -p ~/.config/powershell/  
RUN mkdir -p ~/.local/share/powershell/Modules  
RUN unzip $POWERCLI_PACKAGE -d ~/.local/share/powershell/Modules  
RUN unzip $POWERCLI_VDS_PACKAGE -d ~/.local/share/powershell/Modules  
  
# Change the default PowerShell profile to include PowerCLI startup  
RUN mv ~/Start-PowerCLI.ps1
~/.config/powershell/Microsoft.PowerShell_profile.ps1  
  
# Add PowervRA  
RUN wget
https://github.com/jakkulabs/PowervRA/releases/download/v2.0.0/PowervRA.zip  
RUN unzip PowervRA.zip -d ~  
RUN mv PowervRA ~/.local/share/powershell/Modules/  
RUN rm -f PowervRA  
  
USER root  
RUN apt-get update \  
&& apt-get -y install ca-certificates \  
htop \  
vim \  
nano \  
make \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
RUN chown -R powershell:powershell /home/powershell/ && chmod -R 777
/home/powershell  
USER powershell  
#Allow connections to servers with non-verified CA certificates  
RUN powershell Set-PowerCLIConfiguration -InvalidCertificateAction Ignore
-Confirm:\$false  
USER root

