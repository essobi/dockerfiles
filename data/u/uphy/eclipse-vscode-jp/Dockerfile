FROM uphy/ubuntu-desktop-jp:16.04  
  
# Install development tools.  
RUN apt-get update && \  
apt-get install -y \  
openjdk-8-jdk \  
openjfx \  
git \  
&& \  
apt-get autoclean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Eclipse  
RUN mkdir -p /usr/local/eclipse && \  
wget -qO-
http://mirror.downloadvn.com/eclipse/technology/epp/downloads/release/oxygen/R/eclipse-
java-oxygen-R-linux-gtk-x86_64.tar.gz | tar zx --strip-components=1 -C
/usr/local/eclipse && \  
ln -s /usr/local/eclipse/eclipse /usr/local/bin/eclipse  
  
# Install Maven  
RUN mkdir -p /usr/local/maven && \  
wget -qO-
http://ftp.tsukuba.wide.ad.jp/software/apache/maven/maven-3/3.5.0/binaries/apache-
maven-3.5.0-bin.tar.gz | tar zx --strip-components=1 -C /usr/local/maven && \  
ln -s /usr/local/maven/bin/mvn /usr/local/bin  
  
# Install Visual Studio Code  
RUN mkdir -p /usr/local/vscode && \  
wget -qO- https://go.microsoft.com/fwlink/?LinkID=620884 | tar zx --strip-
components=1 -C /usr/local/vscode && \  
ln -s /usr/local/vscode/code /usr/local/bin/code && \  
/usr/local/vscode/bin/code --user-data-dir='.' \--install-extension
lukehoban.Go  
  
# Install Golang  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
add-apt-repository ppa:longsleep/golang-backports && \  
apt-get update && \  
apt-get install -y golang-go && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
ENV GOHOME=/root/go \  
GOPATH=/root/go \  
PATH=$PATH:$GOHOME/bin  
# Install Golang development tools  
RUN go get \  
github.com/nsf/gocode \  
github.com/rogpeppe/godef \  
github.com/golang/lint/golint \  
github.com/lukehoban/go-find-references \  
github.com/lukehoban/go-outline \  
sourcegraph.com/sqs/goreturns \  
golang.org/x/tools/cmd/gorename \  
github.com/tpng/gopkgs \  
github.com/newhook/go-symbols  
  
COPY files /

