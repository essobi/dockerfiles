# This is VMware Command line tools and contrib  
# docker build . -t vmutils --compress --rm --squash  
# docker run -ti vmutils  
FROM ubuntu:artful  
LABEL MAINTAINER="Frederic Jacquet <fred@ljf.ch>"  
# Set the working directory to /root  
WORKDIR /root  
VOLUME "/root/src"  
ENV http_proxy ""  
ENV ftp_proxy ""  
ADD VMware-vSphere-CLI-6.5.0-4566394.x86_64.tar.gz /tmp/  
ADD VMware-ovftool-4.2.0-5965791-lin.x86_64.bundle /tmp/  
ADD VMware-vix-disklib-6.5.2-6195444.x86_64.tar.gz /tmp/  
ADD VMware_vRealize_CloudClient-4.4.0-5511232.zip /tmp/  
## -------- vSphere -------- ##  
RUN apt-get update && apt-get install -yq curl  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -  
RUN curl https://packages.microsoft.com/config/ubuntu/17.04/prod.list |tee
/etc/apt/sources.list.d/microsoft.list  
RUN curl
https://communities.cisco.com/servlet/JiveServlet/download/74217-3-149644/ucspowertoolcore.zip
-o /tmp/ucspowertoolcore.zip  
# Install vCLI Pre-Reqs  
RUN apt-get update && apt-get install -yq build-essential lsb e2fsprogs
inetutils-ping ash git \  
expect kmod perl-doc wget uuid uuid-dev libssl-dev libffi-dev \  
libxml2-dev libxslt-dev libxml-libxml-perl libarchive-zip-perl \  
libmodule-build-perl libextutils-makemaker-cpanfile-perl libuuid-perl \  
libcrypt-ssleay-perl libclass-methodmaker-perl libdata-dump-perl \  
libsoap-lite-perl libdevel-stacktrace-perl libclass-data-inheritable-perl \  
libconvert-asn1-perl libcrypt-openssl-rsa-perl libcrypt-x509-perl \  
libexception-class-perl libpath-class-perl libsocket6-perl \  
libio-socket-inet6-perl libnet-inet6glue-perl python python-dev \  
python-pip python-virtualenv ruby-full gem default-jre \  
golang golang-context-dev powershell && apt-get clean  
  
# Install vCLI https://developercenter.vmware.com/web/dp/tool/vsphere_cli/5.5  
RUN echo yes | cpan && cpan install UUID::Random  
RUN yes | /tmp/vmware-vsphere-cli-distrib/vmware-install.pl -d && rm -rf
/tmp/vmware-vsphere-cli-distrib  
# Install VMware OVFTool http://vmware.com/go/ovftool  
RUN yes | /bin/bash /tmp/VMware-ovftool-4.2.0-5965791-lin.x86_64.bundle
--required --console && rm -f /tmp/VMware-
ovftool-4.2.0-5965791-lin.x86_64.bundle  
# Install VDDK  
RUN mv /tmp/vmware-vix-disklib-distrib/ /root/src && rm -rf /tmp/vmware-vix-
disklib-distrib  
# Install Cloud Client https://my.vmware.com/group/vmware/get-
download?downloadGroup=CLOUDCLIENT_420&productId=601  
RUN unzip /tmp/VMware_vRealize_CloudClient-4.4.0-5511232.zip -d /root && rm
-rf /tmp/VMware_vRealize_CloudClient-4.4.0-5511232.zip  
# Add William Lams awesome scripts from vGhetto Script Repository  
RUN mkdir /root/vghetto && git clone https://github.com/lamw/vghetto-
scripts.git /root/vghetto  
# Install pyVmomi (vSphere SDK for Python)  
RUN git clone https://github.com/vmware/pyvmomi.git /root/pyvmomi  
# Install rbVmomi & RVC & RaaS CLI  
RUN gem install rbvmomi rvc RaaS  
## -------- vCloud Director -------- ##  
# Install vcloud-tools  
RUN gem install --no-rdoc --no-ri vcloud-tools  
# Install vCloud SDK for Python  
RUN easy_install -U pip  
## -------- vCloud Air -------- ##  
# Install vca-cli  
RUN pip install vca-cli pyvcloud  
# Install govc CLI  
RUN go get github.com/vmware/govmomi/govc  
# Install PowerCLI  
RUN mkdir -p /root/.local/share/powershell/Modules && unzip
/tmp/ucspowertoolcore.zip -d /root/.local/share/powershell/Modules && rm -rf
/tmp/ucspowertoolcore.zip  
RUN pwsh -ex unrestricted -noni -Command Set-PSRepository -Name PSGallery
-InstallationPolicy Trusted  
RUN pwsh -ex unrestricted -noni -Command Install-Module -name VMware.PowerCLI  
RUN pwsh -ex unrestricted -noni -Command Install-Module -name PowerNSX  
RUN pwsh -ex unrestricted -noni -Command Install-Module -Name VPLEX-Powershell  
RUN pwsh -ex unrestricted -noni -Command Install-Module -Name Unity-Powershell  
RUN pwsh -ex unrestricted -noni -Command Install-Module -Name IsilonPlatform  
RUN echo "alias start-usc=pwsh –NoExit –File
~/.local/share/powershell/Modules/Start-UcsPowerTool.ps1" >> ./.bashrc  
# Run Bash when the image starts  
CMD ["/bin/bash"]

