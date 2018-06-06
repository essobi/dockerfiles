# set base os  
FROM carpenike/baseimage  
  
MAINTAINER carpenike <carpenike@gmail.com>  
  
# set some environment variables for mariadb to give us our paths  
ENV INSTALL_LIST="mono-devel fsharp mono-vbnc nuget"  
  
RUN apt-get update && \  
apt-get install -y curl && \  
rm -rf /var/lib/apt/lists/*  
# update apt and install packages  
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \  
echo "deb http://download.mono-project.com/repo/debian wheezy/snapshots/3.10.0
main" > /etc/apt/sources.list.d/mono-xamarin.list && \  
echo "deb http://download.mono-project.com/repo/debian 310-security main" >>
/etc/apt/sources.list.d/mono-xamarin.list && \  
apt-get -qy update && \  
apt-get install \  
$INSTALL_LIST -qy && \  
  
# clean up  
apt-get clean -y && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mozroots --machine --import --sync --quiet  

