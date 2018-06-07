# From base kali  
FROM kalilinux/kali-linux-docker  
  
# Set working dir  
WORKDIR /root/  
  
ENV LC_ALL C.UTF-8  
# kali installs  
RUN apt-get update && apt-get upgrade -y && apt-get install -y \  
locales \  
nmap \  
masscan \  
hping3 \  
curl \  
traceroute \  
sqlmap \  
exploitdb \  
python-impacket \  
man \  
amap \  
aha \  
whatweb \  
php7.0 \  
python-pip \  
python-dev \  
rubygems \  
rubygems-integration \  
build-essential \  
patch \  
ruby-dev \  
zlib1g-dev \  
liblzma-dev \  
skipfish \  
uniscan \  
gobuster \  
clusterd \  
zsh \  
emacs25-nox \  
dnsutils \  
git \  
openssh-client \  
tmux \  
bpython \  
seclists \  
commix \  
libsqlite3-dev \  
host \  
dnsrecon \  
fimap \  
theharvester \  
joomscan \  
python-pyx \  
python-matplotlib \  
python-ecdsa \  
python3-pip \  
python3-dev \  
python-faraday \  
tcpdump \  
libxml2-utils \  
sslscan \  
wpscan \  
libglib2.0-dev \  
msfpc \  
metasploit-framework \  
dirb && \  
apt-get -y autoremove && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/*
/var/tmp/*  
  
RUN pip install \  
pwntools \  
python-nmap \  
requests \  
shodan \  
httplib2 \  
pyip \  
truffleHog \  
pycrypto \  
pyopenssl \  
pyftpdlib \  
r2pipe \  
capstone && \  
rm -r /root/.cache  
  
RUN gem install \  
ruby-nmap \  
net-http-persistent \  
mechanize \  
text-table \  
sqlite3 && \  
rm -r /root/.gem  
  
RUN mkdir -p /opt/data/  
  
RUN yes | cpan install Switch  
  
# GitHub stuff  
RUN git clone https://github.com/0xsauby/yasuo /opt/yasuo/ && \  
git clone https://github.com/drwetter/testssl.sh /opt/testssl && \  
git clone https://github.com/anexia-it/winshock-test /opt/winshock-test && \  
git clone https://github.com/vulnersCom/getsploit /opt/getsploit && \  
git clone https://github.com/Dionach/CMSmap /opt/cmsmap && \  
git clone https://github.com/m4ll0k/Spaghetti /opt/Spaghetti && \  
git clone https://github.com/DanMcInerney/xsscrapy /opt/xsscrapy && \  
cd /opt/xsscrapy && \  
pip install -r ./requirements.txt && \  
cd /opt/Spaghetti && \  
pip install -r ./requirements.txt && \  
apt-get -y autoremove && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/*
/var/tmp/*  
  
# for faraday-pro  
RUN echo 'p-2.6.3' > /usr/share/python-faraday/VERSION  
  
# ZSH  
RUN git clone --recursive https://github.com/sorin-ionescu/prezto.git
"${ZDOTDIR:-$HOME}/.zprezto" && \  
ln -s ~/.zprezto/runcoms/zlogin ~/.zlogin && \  
ln -s ~/.zprezto/runcoms/zlogout ~/.zlogout && \  
ln -s ~/.zprezto/runcoms/zpreztorc ~/.zpreztorc && \  
ln -s ~/.zprezto/runcoms/zprofile ~/.zprofile && \  
ln -s ~/.zprezto/runcoms/zshenv ~/.zshenv && \  
ln -s ~/.zprezto/runcoms/zshrc ~/.zshrc && \  
echo "export TERM=screen-256color" >> ~/.zshrc && \  
echo "unset TMPDIR" >> ~/.zshrc && \  
echo "alias em=emacs" >> ~/.zshrc && \  
echo "alias rm=rm" >> ~/.zshrc && \  
echo "alias phphttpd='php -S 0.0.0.0:8080'" >> ~/.zshrc && \  
echo "alias pyhttpd='python -m SimpleHTTPServer 8080'" >> ~/.zshrc && \  
echo "alias pyftpd='python -m pyftpdlib'" >> ~/.zshrc && \  
echo "alias msfconsole='service postgresql start; msfdb init; msfconsole -q'"
>> $HOME/.zshrc  
  
# set ZSH shell as entry point  
ENTRYPOINT ["/bin/zsh"]  

