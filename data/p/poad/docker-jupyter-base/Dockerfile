FROM python:slim-stretch  
  
LABEL Kenji Saito "ken-yo@mbr.nifty.com"  
  
## ensure locale is set during build  
ENV LANG C.UTF-8  
ENV SBT_VERSION 1.1.6  
ENV SBT_HOME /usr/local/sbt  
ENV SCALA_VERSION 2.12.6  
ENV PATH ${PATH}:${SBT_HOME}/bin  
  
ENV HASKELL_VERSION "lts-11.12"  
ENV GHC_VERSION "8.2.2"  
ENV OCAML_VERSION "4.06.1"  
ENV DEBIAN_FRONTEND noninteractive  
  
USER root  
  
WORKDIR /root/  
  
# Fix the update-alternatives bugs  
RUN mkdir -p /usr/share/man/  
RUN mkdir -p /usr/share/man/man1  
  
ENV PATH /root/.local/bin:${PATH}  
  
RUN apt-get -qq update && \  
apt-get -qq -y upgrade && \  
apt-get install -qq -y --no-install-recommends \  
apt-utils \  
apt-transport-https \  
gnupg \  
dirmngr \  
curl \  
wget \  
software-properties-common && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Haskell  
RUN apt-get -qq update && \  
apt-get install -qq -y --no-install-recommends \  
binutils cpp cpp g++ g++-6 gcc git git-man less libasan3 libatomic1 \  
libbsd0 libc-dev-bin libc6-dev libcilkrts5 libedit2 liberror-perl \  
libffi-dev libgcc-6-dev libgmp-dev libgmpxx4ldbl libgomp1 libgpm2 libisl15 \  
libitm1 liblsan0 libmpc3 libmpfr4 libmpx2 libncurses5 libperl5.24 libpopt0 \  
libquadmath0 libstdc++-6-dev libtsan0 libubsan0 libx11-6 libx11-data libxau6 \  
libxcb1 libxdmcp6 libxext6 libxmuu1 linux-libc-dev make manpages \  
manpages-dev openssh-client patch perl perl-modules-5.24 rename rsync xauth \  
xz-utils zlib1g-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN apt-get -qq update && \  
export STACK_VERSION=$(curl -sSL https://get.haskellstack.org/ | grep -h
STACK_VERSION= | sed "s/STACK_VERSION=//" | sed "s/\"//g") && \  
curl -fSL
https://github.com/commercialhaskell/stack/releases/download/v${STACK_VERSION}/stack-${STACK_VERSION}-linux-x86_64.tar.gz
-o stack.tar.gz && \  
curl -fSL
https://github.com/commercialhaskell/stack/releases/download/v${STACK_VERSION}/stack-${STACK_VERSION}-linux-x86_64.tar.gz.asc
-o stack.tar.gz.asc && \  
export GNUPGHOME="$(mktemp -d)" && \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
C5705533DA4F78D8664B5DC0575159689BEFB442 && \  
gpg --batch --verify stack.tar.gz.asc stack.tar.gz && \  
tar -xf stack.tar.gz -C /usr/bin --strip-components=1 && \  
stack --resolver ${HASKELL_VERSION} config set system-ghc --global true && \  
stack --resolver ${HASKELL_VERSION} install gtk2hs-buildtools --fast -j 4 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /stack.tar.gz.asc /stack.tar.gz  
  
RUN apt-get -qq update && \  
apt-get install -qq -y --no-install-recommends \  
build-essential \  
ca-certificates \  
g++ gcc git \  
libblas-dev \  
libc6-dev \  
libcairo2-dev \  
libffi-dev \  
liblapack-dev \  
libmagic-dev \  
libpango1.0-dev \  
libsqlite3-0 \  
libsqlite3-dev \  
libtinfo-dev \  
libzmq3-dev \  
make \  
unzip \  
xz-utils \  
zlib1g-dev && \  
apt-get autoremove --purge -y && \  
apt-get clean && \  
rm -rf /tmp/* && \  
rm -rf /var/lib/apt/lists/*  
  
RUN echo "deb http://ftp.jp.debian.org/debian $(lsb_release -sc)-backports
main contrib non-free" > /etc/apt/sources.list.d/backports.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys F6BC817356A3D45E && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 308C15A29AD198E9 && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys FF3AEACEF6F88286  
  
RUN echo "deb http://ppa.launchpad.net/longsleep/golang-backports/ubuntu
xenial main" > /etc/apt/sources.list.d/golang-go-backports.list && \  
echo "deb-src http://ppa.launchpad.net/longsleep/golang-backports/ubuntu
xenial main " >> /etc/apt/sources.list.d/golang-go-backports.list && \  
gpg --keyserver keyserver.ubuntu.com --recv-keys
C5705533DA4F78D8664B5DC0575159689BEFB442 && \  
curl -sL https://deb.nodesource.com/setup_8.x | bash - && \  
curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
RUN apt-get update -qq && \  
apt-get install -qq -y --no-install-recommends \  
yarn \  
aspcud \  
bzip2 \  
ca-certificates curl \  
g++ gcc git \  
golang-1.10-go \  
libblas-dev \  
libc6-dev \  
libcairo2-dev \  
libffi-dev \  
liblapack-dev \  
libmagic-dev \  
libpango1.0-dev \  
libsqlite3-0 \  
libsqlite3-dev \  
libssl-dev \  
libcrypto++6 \  
libcrypto++-dev \  
libtinfo-dev \  
libzmq3-dev \  
libczmq-dev \  
libtool build-essential autoconf automake \  
make \  
m4 \  
nodejs \  
ocaml-nox \  
pandoc python3-pip \  
patch \  
pkg-config \  
unzip \  
xz-utils \  
zlib1g-dev \  
openjdk-8-jdk \  
erlang erlang-dev elixir rebar && \  
apt-get upgrade -qq -y && \  
apt-get autoremove --purge -y && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
ENV PATH ${PATH}:/usr/lib/go-1.10/bin  
ENV GOPATH /root/go  
  
# Install Python and Jupyter  
RUN curl -s https://bootstrap.pypa.io/get-pip.py | python && \  
pip install -U setuptools pip && \  
pip install jupyter notebook jupyterlab \  
scipy scikit-learn pygments && \  
pip --no-cache-dir install --trusted-host pypi.python.org pypandoc && \  
pip --no-cache-dir install pandas py4j lxml && \  
pip install --upgrade beautifulsoup4 html5lib  
RUN curl -s https://bootstrap.pypa.io/get-pip.py | python3.6 && \  
pip3 install -U setuptools pip && \  
pip3 install jupyter notebook jupyterlab \  
scipy scikit-learn pygments && \  
pip3 --no-cache-dir install --trusted-host pypi.python.org pypandoc && \  
pip3 --no-cache-dir install pandas py4j lxml && \  
pip3 install --upgrade beautifulsoup4 html5lib && \  
pip3 install --upgrade pip && \  
pip3 install scipy scikit-learn pygments ipykernel ipython \  
numpy matplotlib python-highcharts pandas-highcharts \  
seaborn scikit-image \  
sympy cython patsy statsmodels dill bokeh h5py pandas \  
jupyter_nbextensions_configurator \  
jupyter_contrib_nbextensions && \  
jupyter serverextension enable \--py jupyterlab --sys-prefix && \  
jupyter nbextension enable \--py widgetsnbextension && \  
jupyter notebook --generate-config --allow-root && \  
pip3 install --upgrade jupyter_core jupyter_client  
  
# Install sbt  
RUN curl -sL
"https://github.com/sbt/sbt/releases/download/v${SBT_VERSION}/sbt-${SBT_VERSION}.tgz"
| tar -xz -C /usr/local  
  
# Install Rust  
RUN cd /tmp; curl -o rustup.sh https://sh.rustup.rs && sh rustup.sh -y && true  
ENV PATH $PATH:/root/.cargo/bin  
  
# Install IHaskell  
ENV PATH $(stack path --local-install-root)/bin:$(stack path --snapshot-
install-root)/bin:$(stack path --compiler-
bin):/root/.local/bin:/usr/local/sbin:/usr/local/bin:${PATH}  
WORKDIR /root  
RUN cd /root && \  
git clone https://github.com/gibiansky/IHaskell.git /root/IHaskell && \  
mkdir -p /root/.local/bin && \  
cd /root/IHaskell && \  
pip3 install -r requirements.txt  
ENV STACK_YAML "/root/IHaskell/stack.yaml"  
RUN cd /root/IHaskell && \  
stack setup  
  
RUN update-java-alternatives -s java-1.8.0-openjdk-amd64  
  
# OCaml  
RUN wget https://raw.github.com/ocaml/opam/master/shell/opam_installer.sh -O -
| sh -s /usr/local/bin && \  
opam init && \  
opam switch ${OCAML_VERSION} && \  
eval `opam config env`  
  
# Install and upgrade node.js  
RUN npm install -g npm  
  
RUN rm -rf "$GNUPGHOME"  

