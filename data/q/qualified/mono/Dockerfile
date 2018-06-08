FROM buildpack-deps:xenial  
  
RUN set -ex; \  
useradd --create-home codewarrior; \  
ln -s /home/codewarrior /workspace;  
  
RUN set -ex; \  
apt-key adv \  
\--keyserver hkp://keyserver.ubuntu.com:80 \  
\--recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \  
; \  
# use "wheezy/snapshots/4.8.0.524" to pin Mono 4.8.0.524  
echo "deb http://download.mono-project.com/repo/debian
wheezy/snapshots/4.8.0.524 main" > /etc/apt/sources.list.d/mono-official.list;
\  
apt-get update; \  
apt-get install -y --no-install-recommends \  
# > The package mono-complete should be installed to install everything -  
# > this should cover most cases of "assembly not found" errors.  
mono-complete \  
# > The package referenceassemblies-pcl should be installed for PCL
compilation support -  
# > this will resolve most cases of "Framework not installed: .NETPortable"
errors  
# > during software compilation.  
# PCL = Portable Class Library  
# https://developer.xamarin.com/guides/cross-
platform/application_fundamentals/pcl/introduction_to_portable_class_libraries/  
# referenceassemblies-pcl \  
# > The package mono-xsp4 should be installed for running ASP.NET
applications.  
mono-xsp4 \  
# fsharpc and fsharpi  
fsharp \  
# Fix Could not find file "/etc/localtime"  
tzdata \  
; \  
rm -rf /var/lib/apt/lists/* /tmp/*;  
  
COPY rootfs/runner /runner  
  
USER codewarrior  
ENV USER=codewarrior \  
HOME=/home/codewarrior  
WORKDIR /workspace  

