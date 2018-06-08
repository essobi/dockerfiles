from ubuntu:latest  
maintainer Sergey Kolos <skolos@gopherlab.com>  
  
# Mercurial  
run echo 'deb http://ppa.launchpad.net/mercurial-ppa/releases/ubuntu precise
main' > /etc/apt/sources.list.d/mercurial.list  
run echo 'deb-src http://ppa.launchpad.net/mercurial-ppa/releases/ubuntu
precise main' >> /etc/apt/sources.list.d/mercurial.list  
run apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 323293EE  
  
# Install dependencies  
run apt-get update  
run apt-get install -y curl git bzr mercurial build-essential  
  
# Install Go  
run curl -s https://go.googlecode.com/files/go1.2.1.linux-amd64.tar.gz | tar
-v -C /usr/local/ -xz  
env PATH
/go:/usr/local/go/bin:/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/bin:/sbin  
env GOPATH /go  
env GOROOT /usr/local/go  
  
# Install goxc  
run mkdir /go  
run go get github.com/laher/goxc  
run cp /go/bin/goxc /usr/bin  
run goxc -t  
run rm -rf /go  
run echo "alias ls='ls --color=auto'" >> /etc/bash.bashrc  
run echo "alias grep='grep --color=auto'" >> /etc/bash.bashrc  
run echo "PS1='\\[\e[1;34m\\]\w\\[\e[m\\] \\[\e[1;32m\\]\$\\[\e[m\\]
\\[\e[1;37m\\]'" >> /etc/bash.bashrc  
run echo "cd /go/src" >> /etc/bash.bashrc  

