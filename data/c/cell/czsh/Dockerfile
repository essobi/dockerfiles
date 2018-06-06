#golang env  
FROM ubuntu:rolling as golang-tools  
  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -qy --no-install-recommends
wget git ca-certificates  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -qy golang-go  
  
ENV GOPATH=/tmp/go GOBIN=/usr/local/go/bin PATH=${PATH}:/usr/local/go/bin  
RUN go get -u golang.org/x/tools/cmd/godoc  
RUN go get -u golang.org/x/tools/cmd/goimports  
RUN go get -u golang.org/x/tools/cmd/gorename  
RUN go get -u github.com/nsf/gocode  
RUN go get -u github.com/rogpeppe/godef  
RUN go get -u github.com/golang/lint/golint  
RUN go get -u github.com/kisielk/errcheck  
RUN go get -u github.com/jstemmer/gotags  
RUN go get -u github.com/golang/dep/cmd/dep  
  
#RUN go get -u github.com/Originate/git-town  
RUN go get -u github.com/interesse/git-town  
RUN go get -u github.com/erning/gorun  
RUN go get -u mvdan.cc/sh/cmd/shfmt  
  
#docker-compose and dc  
FROM ubuntu:rolling as dc  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -qy --no-install-recommends
sudo curl git ca-certificates  
RUN git clone https://github.com/Cellophan/scripts.git /tmp/scripts  
RUN find /tmp/scripts -maxdepth 1 -type f -executable -exec cp {}
/usr/local/bin/ \; &&\  
/usr/local/bin/dc install  
RUN curl -sSL \  
https://github.com/docker/compose/releases/download/1.21.2/docker-
compose-$(uname -s)-$(uname -m) \  
>> /usr/local/bin/docker-compose  
RUN chmod +x /usr/local/bin/docker-compose  
  
#container-diff #container-structure-test  
#from http://opensource.googleblog.com/2018/01/container-structure-tests-unit-
tests.html  
FROM ubuntu:rolling as container-tools  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -qy --no-install-recommends
curl ca-certificates  
RUN curl -L https://storage.googleapis.com/container-diff/latest/container-
diff-linux-amd64 >/usr/local/bin/container-diff  
RUN curl -L https://storage.googleapis.com/container-structure-
test/latest/container-structure-test >/usr/local/bin/container-structure-test  
RUN chmod +x /usr/local/bin/*  
  
#Main  
FROM cell/playground  
ENV DOCKER_IMAGE="cell/czsh"  
#zsh and oh-my-zsh  
#https://hub.docker.com/r/nacyot/ubuntu/~/dockerfile/  
RUN apt-get update &&\  
apt-get install -qy --no-install-recommends zsh &&\  
apt-get clean -y && rm -rf /var/lib/apt/lists/* &&\  
git clone https://github.com/robbyrussell/oh-my-zsh.git /etc/skel/.oh-my-zsh
&&\  
ln -s /etc/skel/.oh-my-zsh /root &&\  
ln -s /etc/skel/.zshrc /root  
  
#agnoster  
RUN git clone \--depth 1 https://github.com/Cellophan/agnoster-zsh-theme
/etc/skel/.oh-my-zsh/custom/themes/agnoster-zsh-theme &&\  
ln -s /etc/skel/.oh-my-zsh/custom/themes/agnoster-zsh-theme/agnoster.zsh-theme
/etc/skel/.oh-my-zsh/custom/themes  
  
#fzf  
RUN apt-get update &&\  
apt-get install -qy --no-install-recommends silversearcher-ag &&\  
apt-get clean -y && rm -rf /var/lib/apt/lists/* &&\  
git clone https://github.com/junegunn/fzf.git /etc/skel/.oh-my-
zsh/custom/plugins/fzf &&\  
/etc/skel/.oh-my-zsh/custom/plugins/fzf/install --bin &&\  
git clone https://github.com/Treri/fzf-zsh.git /etc/skel/.oh-my-
zsh/custom/plugins/fzf-zsh  
  
#powerline  
RUN apt-get update &&\  
apt-get install -qy --no-install-recommends wget dconf-cli &&\  
apt-get clean -y && rm -rf /var/lib/apt/lists/* &&\  
mkdir -p /etc/skel/.fonts /etc/skel.config/fontconfig/conf.d &&\  
wget -q -P /etc/skel/.fonts/
https://github.com/powerline/powerline/raw/develop/font/PowerlineSymbols.otf
&&\  
wget -q -P /etc/skel/.config/fontconfig/conf.d
https://github.com/powerline/powerline/raw/develop/font/10-powerline-
symbols.conf &&\  
apt-get remove -y wget  
  
RUN apt-get update &&\  
apt-get install -qy --no-install-recommends fontconfig locales &&\  
apt-get clean -y && rm -rf /var/lib/apt/lists/* &&\  
locale-gen en_US.UTF-8 en_US &&\  
DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales &&\  
/usr/sbin/update-locale LANG=C.UTF-8 &&\  
chsh -s /bin/zsh  
  
RUN apt-get update &&\  
DEBIAN_FRONTEND=noninteractive apt-get install -qy --no-install-recommends
wget git ca-certificates golang-go &&\  
apt-get remove -y wget  
  
#Imports  
COPY \--from=dc /usr/local/bin/* /usr/local/bin/  
COPY \--from=golang-tools /usr/local/go /usr/local/go  
#COPY --from=drone/cli /bin/drone /usr/local/bin/  
COPY \--from=container-tools /usr/local/bin/* /usr/local/bin/  
  
#make  
RUN apt-get update &&\  
apt-get install -qy --no-install-recommends make &&\  
apt-get clean -y && rm -rf /var/lib/apt/lists/*  
  
COPY material/payload /opt/payload/  
COPY material/scripts /usr/local/bin/  
COPY material/profile.d /etc/profile.d/  
COPY material/virtualenv.sudoers /etc/sudoers.d/virtualenv  
COPY material/skel/* /etc/skel/  
  

