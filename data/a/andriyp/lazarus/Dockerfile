FROM shadowrobot/build-tools:trusty-indigo  
  
MAINTAINER "Andriy Petlovanyy"  
  
LABEL Description="This image allows to run Lazarus UI in Docker container"
Vendor="Andriy Petlovanyy" Version="1.0"  
  
RUN set -x && \  
export
downloads_url="http://downloads.sourceforge.net/project/lazarus/Lazarus%20Linux%20amd64%20DEB/Lazarus%201.6.2"
&& \  
  
echo "Installing needed libraries" && \  
apt-get update && \  
apt-get install -y wget binutils gcc libgtk2.0-0 libgtk2.0-dev psmisc gdb && \  
  
echo "Downloading and installing Debians" && \  
cd /tmp && \  
wget "${downloads_url}/fpc_3.0.0-151205_amd64.deb" && \  
dpkg -i fpc_3.0.0-151205_amd64.deb && \  
wget "${downloads_url}/fpc-src_3.0.0-151205_amd64.deb" && \  
dpkg -i fpc-src_3.0.0-151205_amd64.deb && \  
wget "${downloads_url}/lazarus-project_1.6.2-1_amd64.deb" && \  
dpkg -i lazarus-project_1.6.2-1_amd64.deb && \  
  
echo "Removing cache" && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
  
CMD ["/usr/bin/terminator"]  

