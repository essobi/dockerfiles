FROM skegio/clojure:java8  
  
# Holen  
RUN wget https://github.com/holen-
app/holen/releases/download/v0.3.0/holen_linux_amd64 -O /usr/local/bin/holen
&& \  
chmod a+x /usr/local/bin/holen  
  
# git annex  
RUN wget -O- http://neuro.debian.net/lists/xenial.us-tn.full >
/etc/apt/sources.list.d/neurodebian.sources.list && \  
wget -O- http://neuro.debian.net/_static/neuro.debian.net.asc >
/root/neuro.debian.key && \  
apt-key add /root/neuro.debian.key && rm /root/neuro.debian.key && \  
apt-get update && apt-get install -y git-annex-standalone  
  
# tmux  
RUN add-apt-repository ppa:hnakamur/tmux && \  
apt-get update && apt-get install -y tmux  
  
# Neovim and Vim 8.x  
RUN add-apt-repository ppa:jonathonf/vim && \  
add-apt-repository ppa:neovim-ppa/unstable && \  
apt-get update && apt-get install -y vim-nox neovim python-dev python-pip
python3-dev python3-pip && \  
pip install neovim && \  
pip3 install neovim  
  
# need the JDK variant for real Java compiles  
RUN apt update && apt install -y openjdk-8-jdk-headless visualvm  
  
# protobuf compiler install  
RUN wget
https://github.com/google/protobuf/releases/download/v3.5.1/protoc-3.5.1-linux-x86_64.zip
-O /tmp/protoc.zip && \  
unzip -d /usr/local /tmp/protoc.zip bin/protoc && \  
chmod a+x /usr/local/bin/protoc && \  
rm /tmp/protoc.zip  
  
# node and yarn  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && \  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && apt-get install -y nodejs yarn  
  
# other apps  
RUN apt-get update && apt-get install -y mongodb rsync graphviz bc  
  
RUN apt-get update && apt-get install libssl-dev g++ -y && \  
cd /root && git clone https://github.com/AGWA/git-crypt.git && cd git-crypt \  
make && make install && \  
cd .. && rm -rf git-crypt  
  
# clojure 1.9  
RUN wget -O- https://download.clojure.org/install/linux-install-1.9.0.381.sh |
bash -  
  
# planck  
RUN add-apt-repository ppa:mfikes/planck && \  
apt-get update && apt-get install -y planck  
  
RUN echo "AddressFamily inet" >> /etc/ssh/sshd_config  

