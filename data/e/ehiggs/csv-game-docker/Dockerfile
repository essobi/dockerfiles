FROM debian:testing  
  
# File Author / Maintainer  
MAINTAINER Ewan Higgs <ewan_higgs@yahoo.co.uk>  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
ENV AWK_DEPS="gawk mawk"  
ENV C_DEPS="libcsv-dev"  
ENV CPP_DEPS="libboost-dev"  
ENV HASKELL_DEPS="ghc libffi-dev libgmp-dev"  
ENV R_DEPS="r-base r-base-dev libopenblas-base"  
ENV PYTHON2_DEPS="python python-dev python-pip"  
ENV PYTHON3_DEPS="python3 python3-dev python3-pip"  
ENV RUBY_DEPS="ruby ruby-dev"  
ENV LUA_DEPS="lua5.1 luajit luarocks"  
ENV OCAML_DEPS="ocaml opam ocaml-findlib"  
ENV PHP_DEPS="php7.0"  
# General tools  
RUN apt-get update && \  
apt-get install \  
ca-certificates \  
curl \  
dirmngr \  
gcc \  
gnupg \  
libc6-dev \  
m4 \  
git \  
sudo \  
swig \  
$AWK_DEPS \  
$C_DEPS \  
$CPP_DEPS \  
$HASKELL_DEPS \  
$R_DEPS \  
$JAVA_DEPS \  
$PYTHON2_DEPS \  
$PYTHON3_DEPS \  
$OCAML_DEPS \  
$RUBY_DEPS \  
$LUA_DEPS \  
$PHP_DEPS \  
-qqy \  
\--no-install-recommends  
  
# Setup Crystal repository  
RUN apt-key adv --keyserver keys.gnupg.net --recv-keys 09617FD37CC06B54; \  
echo "deb https://dist.crystal-lang.org/apt crystal main" >
/etc/apt/sources.list.d/crystal.list  
  
# Install Crystal  
RUN apt-get -q update  
RUN apt-get -q install --no-install-recommends -y crystal  
  
# Oracle Java  
#RUN apt-get -q install --no-install-recommends -y software-properties-common  
#RUN add-apt-repository -y ppa:webupd8team/java  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" |
\  
tee /etc/apt/sources.list.d/webupd8team-java.list; \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" |
\  
tee -a /etc/apt/sources.list.d/webupd8team-java.list; \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886  
RUN apt-get -q update  
  
# Auto-accept the Oracle JDK license  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | \  
/usr/bin/debconf-set-selections  
RUN apt-get -q install --no-install-recommends -y oracle-java8-installer  
  
# Apps that require Java  
RUN apt-get -q install --no-install-recommends -y \  
ant \  
maven  
  
RUN rm -rf /var/lib/apt/lists/*  
  
# Create a user with which to do the rest of the work.  
# Ocaml requires this - but wercker must run as root, so basically wercker
can't  
# work with ocaml.  
#RUN useradd developer -d /home/developer -m -s /bin/bash && \  
# echo developer:developer | chpasswd && \  
# usermod -a -G sudo developer  
# Lua  
RUN luarocks install lpeg  
  
# Julia  
WORKDIR /usr/local  
RUN curl -s
https://julialang-s3.julialang.org/bin/linux/x64/0.6/julia-0.6.2-linux-x86_64.tar.gz
> julia.tar.gz \  
&& tar xzf julia.tar.gz --transform s/julia-d386e40c17/julia/ \  
&& rm julia.tar.gz  
ENV PATH="${PATH}:/usr/local/julia/bin"  
# Haskell  
WORKDIR /  
RUN curl -sSL https://get.haskellstack.org/ | sh  
  
#USER developer  
# Python  
RUN pip install pandas  
# Perl  
# Perl seems to install Text::CSV_XS just fine but still gives error code 8.  
RUN cpan install perl Text::CSV_XS ; exit 0  
# OCaml  
RUN opam init -a && eval $(opam config env) && opam update && opam install -y
csv  
  
USER root  
  
#Rust  
RUN mkdir /rust  
RUN pwd  
WORKDIR /rust  
  
# Rust  
ENV RUST_ARCHIVE=rust-nightly-x86_64-unknown-linux-gnu.tar.gz  
ENV RUST_DOWNLOAD_URL=https://static.rust-lang.org/dist/$RUST_ARCHIVE  
  
RUN curl -fsOSL $RUST_DOWNLOAD_URL \  
&& curl -s $RUST_DOWNLOAD_URL.sha256 | sha256sum -c - \  
&& tar -C /rust -xzf $RUST_ARCHIVE \--strip-components=1 \  
&& rm $RUST_ARCHIVE \  
&& ./install.sh  
  
# Ruby  
RUN gem install fastest-csv  
  
# Clojure  
ENV LEIN_ROOT 1  
# Install Leiningen and make executable  
ENV
LEIN_DOWNLOAD_URL=https://raw.githubusercontent.com/technomancy/leiningen/2.6.1/bin/lein  
RUN curl -s $LEIN_DOWNLOAD_URL > /usr/local/bin/lein \  
&& chmod 0755 /usr/local/bin/lein \  
&& /usr/local/bin/lein  
  
# Nim  
WORKDIR /nim  
ENV NIM_VERSION=0.16.0  
ENV NIM_ARCHIVE=nim-$NIM_VERSION.tar.xz  
ENV NIM_DOWNLOAD_URL=https://nim-lang.org/download/$NIM_ARCHIVE  
RUN curl -fsOS $NIM_DOWNLOAD_URL \  
&& curl -s $NIM_DOWNLOAD_URL.sha256 | sha256sum -c - \  
&& tar -C /nim -xf $NIM_ARCHIVE \  
&& rm $NIM_ARCHIVE \  
&& cd nim-$NIM_VERSION \  
&& sh build.sh \  
&& bin/nim c koch \  
&& ./koch tools  
ENV PATH="${PATH}:/nim/nim-${NIM_VERSION}/bin"  
# Golang  
WORKDIR /usr/local  
RUN curl -s https://storage.googleapis.com/golang/go1.9.1.linux-amd64.tar.gz >
go.tar.gz \  
&& tar xzf go.tar.gz \  
&& rm go.tar.gz  
ENV PATH="${PATH}:/usr/local/go/bin"  
# Paratext  
WORKDIR /paratext  
RUN pip install numpy six \  
&& git clone https://github.com/wiseio/paratext.git \  
&& cd paratext/python \  
&& python setup.py install  
  
WORKDIR /  
#USER developer  

