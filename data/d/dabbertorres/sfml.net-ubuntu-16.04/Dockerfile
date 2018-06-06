from dabbertorres/csfml-ubuntu-16.04  
# add mono official repository as Ubuntu's package is super old  
run apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF  
run echo "deb http://download.mono-project.com/repo/ubuntu xenial main" | tee
/etc/apt/sources.list.d/mono-official.list  
  
run apt update  
  
# build dependencies  
run apt install -y \  
mono-devel \  
mono-complete \  
libopentk-cil-dev  
  
# runtime dependencies  
run apt install -y \  
tzdata  
  
# build  
workdir /build  
run git clone https://github.com/SFML/SFML.Net.git  
workdir /build/SFML.Net/build/vc2010  
run xbuild /p:TargetFrameworkVersion="v4.0" /p:Configuration=Release
SFML.net.sln  
workdir /build/SFML.Net/lib/x64  
run cp ./* /usr/local/lib  
  
# make SFML.NET-friendly csfml links  
workdir /usr/local/lib  
run ln -s libcsfml-audio.so libcsfml-audio-2.so  
run ln -s libcsfml-graphics.so libcsfml-graphics-2.so  
run ln -s libcsfml-network.so libcsfml-network-2.so  
run ln -s libcsfml-system.so libcsfml-system-2.so  
run ln -s libcsfml-window.so libcsfml-window-2.so  
  
# clean up  
workdir /  
run rm -r /build  

