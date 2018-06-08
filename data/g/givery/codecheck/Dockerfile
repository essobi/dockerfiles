FROM ubuntu:14.04.2  
ENV OS_USER_NAME codecheck  
WORKDIR /root  
  
# bc is installed for bash script challenge  
RUN apt-get update -qq && \  
apt-get upgrade -qqy && \  
apt-get install -qqy software-properties-common aptitude && \  
apt-add-repository -y ppa:git-core/ppa && \  
apt-get update -qq && \  
apt-get upgrade -qqy && \  
apt-get install -qqy git curl unzip wget bc && \  
rm -rf /var/lib/apt/lists/*  
  
# go  
ENV GOLANG_VERSION=1.6.3  
RUN wget https://storage.googleapis.com/golang/go${GOLANG_VERSION}.linux-
amd64.tar.gz && \  
tar -C /usr/local -xzf go${GOLANG_VERSION}.linux-amd64.tar.gz && \  
rm go${GOLANG_VERSION}.linux-amd64.tar.gz  
ENV PATH $PATH:/usr/local/go/bin  
  
# clang  
RUN apt-get update -qq && \  
apt-get install -qqy \  
gcc-4.8 \  
g++-4.8 \  
&& \  
rm -rf /var/lib/apt/lists/*  
RUN apt-get update -qq && \  
apt-get install -qqy \  
clang-3.4 \  
libclang-common-3.4-dev \  
libclang-3.4-dev \  
libclang1-3.4 \  
libclang1-3.4-dbg \  
libllvm-3.4-ocaml-dev \  
libllvm3.4 \  
libllvm3.4-dbg \  
lldb-3.4 \  
llvm-3.4 \  
llvm-3.4-dev \  
llvm-3.4-runtime \  
clang-modernize-3.4 \  
clang-format-3.4 \  
python-clang-3.4 \  
lldb-3.4-dev \  
&& \  
rm -rf /var/lib/apt/lists/*  
  
# haskell  
RUN apt-add-repository -y ppa:hvr/ghc && \  
apt-get update -qq && \  
apt-get upgrade -qqy && \  
apt-get install -qqy ghc-7.8.4 \  
ghc-haddock \  
ghc-prof \  
alex-3.1.4 \  
happy-1.19.5 \  
cabal-install-1.22 \  
&& \  
rm -rf /var/lib/apt/lists/*  
RUN ln -s /usr/bin/cabal-1.22 /usr/bin/cabal  
RUN cabal update  
RUN cabal install 'hspec < 2.5'  
  
# ocaml  
RUN apt-get update -qq && \  
apt-get upgrade -qq && \  
apt-get install -qqy ocaml && \  
rm -rf /var/lib/apt/lists/*  
  
# perl  
RUN apt-get update -qq && \  
apt-get upgrade -qq && \  
apt-get install -qqy perl && \  
rm -rf /var/lib/apt/lists/*  
  
# ruby  
RUN apt-add-repository -y ppa:brightbox/ruby-ng && \  
apt-get update -qq && \  
apt-get upgrade -qqy && \  
apt-get install -qqy \  
ruby2.3 \  
ruby2.3-dev \  
&& \  
rm -rf /var/lib/apt/lists/*  
RUN gem update  
RUN gem install bundler --version '~>1.15.0'  
RUN gem install rspec --version '~>3.4.0'  
ENV PATH $PATH:/room/.gem/ruby/2.2.0/bin  
  
# python  
RUN apt-get update -qq && \  
apt-get install -qqy build-essential libssl-dev libbz2-dev zlib1g-dev
libreadline-dev libsqlite3-dev && \  
rm -rf /var/lib/apt/lists/*  
RUN VERSION='3.6.1' && \  
wget https://www.python.org/ftp/python/${VERSION}/Python-${VERSION}.tgz && \  
tar zxvf Python-${VERSION}.tgz && \  
cd Python-${VERSION} && \  
./configure && \  
make && \  
make install && \  
cd .. && \  
rm -r Python-${VERSION}.tgz Python-${VERSION}  
RUN VERSION='2.7.11' && \  
wget https://www.python.org/ftp/python/${VERSION}/Python-${VERSION}.tgz && \  
tar zxvf Python-${VERSION}.tgz && \  
cd Python-${VERSION} && \  
./configure && \  
make && \  
make install && \  
cd .. && \  
rm -r Python-${VERSION}.tgz Python-${VERSION}  
RUN curl --silent https://bootstrap.pypa.io/get-pip.py | python3  
RUN curl --silent https://bootstrap.pypa.io/get-pip.py | python  
RUN pip install 'nose>=1.3.7,<1.4.0'  
RUN pip3 install 'nose>=1.3.7,<1.4.0'  
  
# php  
RUN LANG=C.UTF-8 apt-add-repository -y ppa:ondrej/php && \  
apt-get update -qq && \  
apt-get upgrade -qqy && \  
apt-get install -qqy \  
php5.6 \  
php5.6-cli \  
php5.6-common \  
php5.6-curl \  
php5.6-gd \  
php5.6-json \  
php5.6-mcrypt \  
php5.6-mysql \  
php5.6-pgsql \  
php5.6-sqlite \  
&& \  
rm -rf /var/lib/apt/lists/*  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer  
RUN wget https://phar.phpunit.de/phpunit-5.7.phar && \  
chmod +x phpunit-5.7.phar && \  
mv phpunit-5.7.phar /usr/local/bin/phpunit  
  
# mono  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \  
echo "deb http://download.mono-project.com/repo/debian wheezy main" >
/etc/apt/sources.list.d/mono-xamarin.list && \  
apt-get update -qq && \  
apt-get upgrade -qqy && \  
apt-get install -qqy --no-install-recommends \  
mono-complete=5.10.0.140-0xamarin1+debian7b1 \  
monodevelop=5.10.0.871-0xamarin2 \  
monodevelop-nunit=5.10.0.871-0xamarin2 \  
nunit-console=2.6.3+dfsg-1~xamarin8+debian7b1 && \  
rm -rf /var/lib/apt/lists/*  
ENV MONO_PATH /usr/lib/monodevelop/AddIns/NUnit  
  
# nuget  
RUN VERSION='v4.1.0' && \  
wget https://dist.nuget.org/win-x86-commandline/${VERSION}/nuget.exe && \  
mono nuget.exe install Nancy -Version 1.4.3  
  
# gradle  
RUN wget https://services.gradle.org/distributions/gradle-2.7-bin.zip \  
&& unzip gradle-2.7-bin.zip -d /usr/local/share/ \  
&& rm gradle-2.7-bin.zip  
ENV PATH $PATH:/usr/local/share/gradle-2.7/bin  
  
# groovy  
RUN wget https://bintray.com/artifact/download/groovy/maven/apache-groovy-
binary-2.4.5.zip \  
&& unzip apache-groovy-binary-2.4.5.zip -d /usr/local/share/ \  
&& rm apache-groovy-binary-2.4.5.zip  
ENV PATH $PATH:/usr/local/share/groovy-2.4.5/bin  
  
# node  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -qqy nodejs && \  
rm -rf /var/lib/apt/lists/*  
RUN npm install -g \  
codecheck@0.6.5 \  
typescript@2.3.x \  
coffee-script@1.12.x \  
babel-cli@6.24.x \  
mocha@3.4.x \  
chai@4.1.x \  
nightmare@2.10.x \  
grunt-cli@1.2.x \  
gulp@3.9.x \  
webpack@3.0.x  
  
# java  
# This currently contains a dirty hack (the command in parentheses)  
# to fix Oracle's screwup with the download URL  
# Reference:
https://ubuntuforums.org/showthread.php?t=2374686&page=2&s=54df96426d957e93d1559dea42cf4a6b  
RUN apt-add-repository -y ppa:webupd8team/java && \  
apt-get update -qq && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
tee /etc/oracle-java-8-licence-acceptance | /usr/bin/debconf-set-selections &&
\  
(apt-get install -qqy oracle-java8-installer ca-certificates oracle-java8-set-
default maven || \  
sed -i 's|JAVA_VERSION=8u144|JAVA_VERSION=8u152|' /var/lib/dpkg/info/oracle-
java8-installer.* && \  
sed -i 's|PARTNER_URL=http://download.oracle.com/otn-
pub/java/jdk/8u144-b01/090f390dda5b47b9b721c7dfaa008135/|PARTNER_URL=http://download.oracle.com/otn-
pub/java/jdk/8u152-b16/aa0333dd3019491ca4f6ddbe78cdb6d0/|'
/var/lib/dpkg/info/oracle-java8-installer.* && \  
sed -i
's|SHA256SUM_TGZ="e8a341ce566f32c3d06f6d0f0eeea9a0f434f538d22af949ae58bc86f2eeaae4"|SHA256SUM_TGZ="218b3b340c3f6d05d940b817d0270dfe0cfd657a636bad074dcabe0c111961bf"|'
/var/lib/dpkg/info/oracle-java8-installer.* && \  
sed -i 's|J_DIR=jdk1.8.0_144|J_DIR=jdk1.8.0_152|' /var/lib/dpkg/info/oracle-
java8-installer.*) && \  
apt-get install -qqy \  
oracle-java8-installer \  
ca-certificates \  
oracle-java8-set-default \  
maven \  
&& \  
rm -rf /var/lib/apt/lists/*  
  
# scala environment  
RUN mkdir -p /usr/local/share/scala/2.11.7  
RUN wget http://www.scala-lang.org/files/archive/scala-2.11.7.tgz \  
&& tar xzf scala-2.11.7.tgz -C /usr/local/share/scala/2.11.7 \  
&& rm scala-2.11.7.tgz  
RUN ln -s /usr/local/share/scala/2.11.7/scala-2.11.7/bin/scala
/usr/local/bin/scala  
RUN ln -s /usr/local/share/scala/2.11.7/scala-2.11.7/bin/fsc
/usr/local/bin/fsc  
  
# sbt  
RUN mkdir -p /usr/local/share/sbt/0.13.9  
RUN wget https://dl.bintray.com/sbt/native-packages/sbt/0.13.9/sbt-0.13.9.tgz
\  
&& tar xzf sbt-0.13.9.tgz -C /usr/local/share/sbt/0.13.9 \  
&& rm sbt-0.13.9.tgz  
RUN ln -s /usr/local/share/sbt/0.13.9/sbt/bin/sbt /usr/local/bin/sbt  
WORKDIR /root/tmp  
RUN sbt -sbt-version 0.13.9  
RUN git clone https://github.com/shok4a/cache-for-scala-sbt.git  
RUN cd cache-for-scala-sbt && git checkout scala2.11.7-sbt-1.13.5 && sbt
compile  
WORKDIR /root  
RUN rm -r /root/tmp  
  
# activator  
RUN mkdir -p /usr/local/share/activator/1.3.2  
RUN wget http://downloads.typesafe.com/typesafe-activator/1.3.2/typesafe-
activator-1.3.2-minimal.zip \  
&& unzip typesafe-activator-1.3.2-minimal.zip -d
/usr/local/share/activator/1.3.2 \  
&& rm typesafe-activator-1.3.2-minimal.zip  
RUN ln -s /usr/local/share/activator/1.3.2/activator-1.3.2-minimal/activator
/usr/local/bin/activator  
  
RUN apt-get update -qq && \  
apt-get install sbcl && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -O https://beta.quicklisp.org/quicklisp.lisp && \  
echo '(quicklisp-quickstart:install)\n(ql::without-prompting(ql:add-to-init-
file))\n' > install.lisp && \  
sbcl --noinform --quit --load quicklisp.lisp --load install.lisp && \  
mv quicklisp .quicklisp && \  
sed -i -e 's,quicklisp/setup.lisp,.quicklisp/setup.lisp,' .sbclrc && \  
echo '(ql:quickload :prove)\n(quit)\n' > install.lisp && \  
sbcl --noinform --quit --load install.lisp && \  
rm install.lisp quicklisp.lisp  
  
RUN mkdir .go  
ENV GOPATH /root/.go  
ENV PATH $PATH:/usr/local/go/bin  
  
# language-pack-en  
RUN apt-get update -qq && \  
apt-get install language-pack-en -qqy && \  
update-locale LANG=en_US.UTF-8  
ENV LANG=en_US.UTF-8  
# rust  
RUN apt-get update -qq && \  
curl https://sh.rustup.rs -sSf > ./rustup.sh && \  
chmod +x rustup.sh && \  
./rustup.sh -y && \  
rm rustup.sh  
ENV PATH $PATH:/root/.cargo/bin  
  
# headless browser dependencies for frontend tests  
RUN apt-get update && \  
apt-get install -qqy xvfb libnss3-dev && \  
rm -rf /var/lib/apt/lists/*  

