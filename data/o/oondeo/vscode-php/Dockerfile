FROM php-56-centos7:latest  
  
  
#bashrc  
#export PATH=/var/lib/trytond/.npm-
packages/bin:$HOME/.env/bin:$HOME/trytond/bin:$PATH  
#source $HOME/.env/bin/activate  
  
#sudo echo 0 > /proc/sys/kernel/yama/ptrace_scope  
#\--security-opt seccomp=unconfined  
#\--cap-add sys_ptrace  
#deb http://apt.llvm.org/jessie/ llvm-toolchain-jessie-4.0 main  
#deb-src http://apt.llvm.org/jessie/ llvm-toolchain-jessie main  
#wget -O - http://apt.llvm.org/llvm-snapshot.gpg.key|sudo apt-key add -  
  
USER root  
  
#fs.inotify.max_user_watches=524288  
#NODE_PKGS="rh-nodejs4 rh-nodejs4-npm rh-nodejs4-nodejs-nodemon nss_wrapper"  
ENV VSCODE_VERSION="1.16" \  
NODEJS_VERSION=6 NODE_PKGS="" \  
VSCODE_PKGS="git mercurial unzip code" \  
INSTALL_PKGS="socat zsh vim curl xorg-x11-xserver-utils \  
gtk3 liberation-fonts-common liberation-sans-fonts xcb-util" \  
NPM_RUN=start \  
NPM_CONFIG_PREFIX=$HOME/.npm-global \  
PATH=$HOME/node_modules/.bin/:$HOME/.npm-global/bin/:$PATH  
#latest version: code-insiders  
RUN rpm --import https://packages.microsoft.com/keys/microsoft.asc \  
&& sh -c 'echo -e "[code]\nname=Visual Studio
Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc"
> /etc/yum.repos.d/vscode.repo' \  
&& yum install -y --setopt=tsflags=nodocs \  
${VSCODE_PKGS} ${INSTALL_PKGS} ${NODE_PKGS} \  
&& yum clean all -y && rm -rf /var/cache/yum /var/tmp/* /tmp/* /var/log/*
/usr/share/doc/* /usr/share/man/* /root/.cache  
  
ENV FIREFOX_VERSION=56.0.1  
RUN cd /opt && wget
http://ftp.mozilla.org/pub/firefox/releases/${FIREFOX_VERSION}/linux-x86_64/en-
US/firefox-${FIREFOX_VERSION}.tar.bz2 \  
&& tar jxf firefox-${FIREFOX_VERSION}.tar.bz2 && ln -s /opt/firefox/firefox
/usr/local/bin/ \  
&& ln -s /usr/bin/firefox /bin/xdg-open \  
&& rm firefox-${FIREFOX_VERSION}.tar.bz2 \  
mkdir -p /usr/share/zsh/share && curl -L git.io/antigen >
/usr/share/zsh/share/antigen.zsh  
# python-pip python-virtualenv virtualenv python-dev ipython pylint python-
ipdb  
# && ln -s /usr/bin/nodejs /usr/bin/node  
  
#ENV VSCODE_VERSION=1.16.1  
#ENV VSCODE_VERSION=latest  
#RUN curl -o /tmp/vscode.tgz https://vscode-
update.azurewebsites.net/${VSCODE_VERSION}/linux-x64/stable \  
# && tar -zxf /tmp/vscode.tgz  
  
#echo prefix = ${HOME}/.npm-packages > /home/bitnami/.npmrc  
#PATH=${HOME}/.npm-packages/bin:$PATH  
#flake8 yapf  
  
  
# install flat plat theme  
run wget 'https://github.com/nana-4/Flat-
Plat/releases/download/3.20.20160404/Flat-Plat-3.20.20160404.tar.gz'  
run tar -xf Flat-Plat*  
run mv Flat-Plat /usr/share/themes  
run rm Flat-Plat*gz  
run mv /usr/share/themes/Default /usr/share/themes/Default.bak  
run ln -s /usr/share/themes/Flat-Plat /usr/share/themes/Default  
  
# install hack font  
run wget
'https://github.com/chrissimpkins/Hack/releases/download/v2.020/Hack-v2_020-ttf.zip'  
run unzip Hack*.zip  
run mkdir -p /usr/share/fonts/truetype/Hack  
run mv Hack* /usr/share/fonts/truetype/Hack  
run fc-cache -f -v  
  
  
  
  
#additional install  
#RUN apt-get update && apt-get install --no-install-recommends -y dash curl
apt-transport-https \  
# libpq-dev \  
# libldap2-dev \  
# libsasl2-dev \  
# libxslt-dev \  
# libffi-dev \  
# libxml2-dev \  
# && rm -rf /var/cache/apt/* /var/lib/apt/* /var/tmp/* /tmp/* /var/log/*
/usr/share/doc/* /usr/share/man/*  
# RUN apt-get -y update; apt-get install --no-install-recommends -y \  
# freetds-dev \  
# libldap2-dev \  
# libsasl2-dev \  
# libpq-dev \  
# libmariadb-client-lgpl-dev \  
# libmariadb-client-lgpl-dev-compat \  
# sqlite sqlite3 \  
# libsqlite3-dev libmagic-dev \  
# graphviz \  
# libgraphviz-dev \  
# gsfonts \  
# fonts-liberation \  
# fonts-dejavu fonts-freefont-ttf ttf-bitstream-vera fonts-freefont-otf fonts-
lyx xfonts-100dpi xfonts-75dpi texlive-extra-utils texlive-math-extra texlive-
fonts-extra texlive-font-utils texlive ttf-aenigma fonts-roboto \  
# libxml2-dev \  
# libxslt-dev \  
# libjpeg-dev \  
# libreadline-dev \  
# libffi-dev \  
# libncurses5-dev \  
# librabbitmq-dev \  
# rabbitmq-server \  
# libreoffice-script-provider-python \  
# libreoffice-writer \  
# libreoffice-calc \  
# redis-tools \  
# cifs-utils \  
# && curl -L
https://raw.githubusercontent.com/dagwieers/unoconv/master/unoconv >
/usr/local/bin/unoconv \  
# && sed -i '1 s/env.*$/python/' /usr/local/bin/unoconv && chmod +x
/usr/local/bin/unoconv \  
# && pip3 install pyuno \  
# && rm -rf /var/cache/apt/* /var/lib/apt/* /var/tmp/* /tmp/* /var/log/*
/usr/share/doc/* /usr/share/man/* /root/.cache  
RUN yum install -y --setopt=tsflags=nodocs dejavu-fonts liberation-mono-fonts
liberation-narrow-fonts liberation-serif-fonts xorg-x11-font-utils fontconfig
\  
&& yum clean all -y && rm -rf /var/cache/yum /var/tmp/* /tmp/* /var/log/*
/usr/share/doc/* /usr/share/man/* /root/.cache  
  
  
  
user default  
  
COPY zshrc $HOME/.zshrc  
#install plugins  
RUN /usr/bin/code --install-extension felixfbecker.php-intellisense \  
/usr/bin/code --install-extension ecmel.vscode-html-css \  
/usr/bin/code --install-extension felixfbecker.php-debug \  
&& /usr/bin/code --install-extension hbenl.vscode-firefox-debug  
  
# set environment variables  
env BROWSER=/usr/bin/firefox \  
SHELL=/bin/sh \  
DISPLAY=:0  
#to make it working:  
#\- xhost +  
#\- edit lightdm.conf xserver-allow-tcp=true  
#set DISPLAY  
#socat EXEC:'docker exec -i -u root vscode socat unix-l\:/tmp/.X11-unix/X0 -'
unix:/tmp/.X11-unix/X0  
  
  
#CMD ["code --verbose"]  
  
##mount .gitconfig and .ssh dirs  
#docker run -v ~/.ssh:$HOME/.ssh -v ~/.gitconfig:$HOME -e
DISPLAY=172.17.0.1:6000 oondeo/vscode-python  
#pypy3 -m venv env  
#pip3 install pylint  
#PATH=/opt/rh/rh-nodejs${NODEJS_VERSION}/root/usr/bin:${PATH} npm install -g
grunt bower  
#PATH=/opt/app-root/bin:/opt/rh/rh-python36/root/usr/bin:${PATH} pip3 install
pylint ipython ipdb

