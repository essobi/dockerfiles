FROM swiftdocker/swift:3.0.2  
MAINTAINER Kofi Gumbs <h.kofigumbs@gmail.com>  
  
  
### Install libicu52 dependency  
RUN wget -q
http://security.ubuntu.com/ubuntu/pool/main/i/icu/libicu52_52.1-3ubuntu0.4_amd64.deb\  
&& dpkg -i libicu52_52.1-3ubuntu0.4_amd64.deb\  
&& rm libicu52_52.1-3ubuntu0.4_amd64.deb  
  
### Install Anarchy Tools  
RUN _install() {\  
curl -sSL
https://github.com/AnarchyTools/$1/releases/download/$2/$1-$2-linux.atbin.tar.xz\  
| tar -xvJf - bin/$1.atbin > /bin/$1.atbin\  
&& ln -s /bin/$1.atbin/$1 /usr/bin/$1;\  
  
} ; _install atbuild 1.9.1\  
&& _install atpm 1.2.4\  
  
  
  
### Dummy package and task to make sure everything is OK  
  
&& cd /tmp\  
&& echo '(package :name "dummy" :tasks { :test { :tool "shell" :script "echo
Hello, World!" } })' > build.atpkg\  
&& atbuild test  

