FROM phusion/baseimage  
MAINTAINER James kirk <james.kirk84@gmail.com>  
RUN \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \  
echo "deb http://download.mono-project.com/repo/debian wheezy/snapshots/3.12.0
main" | sudo tee /etc/apt/sources.list.d/mono-xamarin.list  
  
RUN apt-get update -y && \  
apt-get install -y mono-devel ca-certificates-mono fsharp mono-vbnc nuget xvfb
firefox=28.0+build2-0ubuntu2 dbus dbus-x11  
  
RUN mozroots --import --sync &&\  
yes | certmgr --ssl -m https://go.microsoft.com &&\  
yes | certmgr -ssl -m https://nugetgallery.blob.core.windows.net &&\  
yes | certmgr -ssl -m https://nuget.org  
  
# This fixes selenium firefox connectivity issues  
RUN dbus-uuidgen > /var/lib/dbus/machine-id  

