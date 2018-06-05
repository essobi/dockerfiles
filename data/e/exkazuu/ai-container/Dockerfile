FROM ubuntu:17.10  
MAINTAINER Kazunori Sakamoto  
  
RUN apt-get update \  
&& apt-get dist-upgrade -y \  
&& apt-get install -y build-essential curl wget dirmngr zip unzip dos2unix \  
&& curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& wget http://master.dl.sourceforge.net/project/d-apt/files/d-apt.list -O
/etc/apt/sources.list.d/d-apt.list \  
&& apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net --recv-keys
EBCF975E5BA24D5E \  
&& apt-get update \  
&& apt-get -y --allow-unauthenticated install --reinstall d-apt-keyring \  
&& apt-get update \  
&& apt-get dist-upgrade -y \  
&& apt-get install -y \  
clang \  
clisp \  
dmd-bin \  
erlang \  
gauche \  
gdc \  
ghc \  
gnu-smalltalk \  
golang \  
libboost-all-dev \  
llvm \  
lua5.3 \  
make \  
mono-complete \  
mono-dmcs \  
mono-xbuild \  
nodejs \  
ocaml-nox \  
python python-pip python-numpy python-scipy \  
python3 python3-pip python3-numpy python3-scipy \  
perl \  
php \  
swi-prolog \  
ruby rbenv ruby-build \  
rustc \  
&& apt-get clean -y \  
&& npm install -g \  
coffee-script \  
typescript \  
livescript \  
&& adduser --disabled-password --gecos "" aicomp \  
&& apt-get purge -y man \  
&& apt-get clean -y \  
&& rm -rf /var/lib/apt/lists/* /tmp/*  
  
USER aicomp  
  
COPY show_versions.sh /home/aicomp/  
  
RUN curl -s https://get.sdkman.io | bash \  
&& echo "-Xms512M -Xmx4G" >> ~/.sbtopts \  
&& echo 'export SDKMAN_DIR="/home/aicomp/.sdkman"' >> ~/.bash_profile \  
&& echo '[[ -s "/home/aicomp/.sdkman/bin/sdkman-init.sh" ]] && source
"/home/aicomp/.sdkman/bin/sdkman-init.sh"' >> ~/.bash_profile \  
&& bash -l -c " \  
yes | sdk install java \  
&& sdk install ant \  
&& sdk install ceylon \  
&& sdk install gradle \  
&& sdk install groovy \  
&& sdk install kotlin \  
&& sdk install maven \  
&& sdk install sbt \  
&& sdk install scala \  
" \  
&& rm -Rf ~/.sdkman/archives/* ~/.sdkman/tmp/* \  
&& pip install chainer keras tensorflow \  
&& pip3 install chainer keras tensorflow \  
&& rbenv install 2.4.0 \  
&& rbenv global 2.4.0 \  
&& echo 'eval "$(rbenv init -)"' >> ~/.bash_profile \  
&& bash -l -c "gem install bundler" \  
&& bash -l ~/show_versions.sh \  
"ant -version | head -n 1" \  
"ceylon -v | head -n 1" \  
"clang --version | head -n 1" \  
"clisp --version | head -n 1" \  
"coffee -v | head -n 1" \  
"dmcs --version | head -n 1" \  
"dmd --version | head -n 1" \  
"erl +V 2>&1 | head -n 1" \  
"gcc --version | head -n 1" \  
"gdc --version | head -n 1" \  
"gem -v | head -n 1" \  
"ghc --version | head -n 1" \  
"g++ --version | head -n 1" \  
"go version | head -n 1" \  
"gosh -V | head -n 1" \  
"gradle -version | head -n 3 | tail -n 1" \  
"groovy --version | head -n 1" \  
"gst -v | head -n 1" \  
"java -version 2>&1 | head -n 1" \  
"javac -version 2>&1 | head -n 1" \  
"kotlin -version | head -n 1" \  
"llc --version | head -n 2 | tail -n 1" \  
"lsc -v | head -n 1" \  
"lua5.3 -v | head -n 1" \  
"make -v | head -n 1" \  
"mcs --version | head -n 1" \  
"mono -V | head -n 1" \  
"mvn -v | head -n 1" \  
"node -v | head -n 1" \  
"npm -v | head -n 1" \  
"ocaml -version | head -n 1" \  
"pip -V | head -n 1" \  
"pip3 -V | head -n 1" \  
"python -V 2>&1 | head -n 1" \  
"python3 -V | head -n 1" \  
"perl -v | sed -n 2P" \  
"php -v | head -n 1" \  
"ruby -v | head -n 1" \  
"rustc --version | head -n 1" \  
"SBT_OPTS='-Xms512M -Xmx4G' sbt about | head -n 5 | tail -n 1" \  
"SBT_OPTS='-Xms512M -Xmx4G' sbt about | head -n 5 | tail -n 1" \  
"scala -version 2>&1 | head -n 1" \  
"swipl --version | head -n 1" \  
"tsc -v | head -n 1" \  
"xbuild --verison | head -n 1" \  
"pip list" \  
"pip3 list" \  
> ~/show_versions \  
&& cat ~/show_versions \  
&& rm -rf ~/show_versions.sh ~/show_versions  

