FROM openjdk:8  
ENV HOME="/root"  
WORKDIR $HOME  
# install Ruby  
# # use rbenv  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends g++ gcc make \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
RUN git clone https://github.com/rbenv/rbenv.git ~/.rbenv  
RUN cd ~/.rbenv \  
&& src/configure \  
&& make -C src  
RUN git clone https://github.com/sstephenson/ruby-build.git
~/.rbenv/plugins/ruby-build  
RUN echo 'export PATH=$HOME/.rbenv/bin:$PATH' >> ~/.bashrc  
# Io  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends cmake g++ gcc libyajl-dev
libpython3.4-dev libgmp-dev libmemcached-dev make \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
RUN git clone \--branch 2015.11.11 --depth 1
https://github.com/stevedekorte/io.git ~/io \  
&& mkdir -p ~/io/build \  
&& cd ~/io/build \  
&& cmake .. \  
&& make install \  
&& rm -fr ~/io  
ENV PATH="/usr/local/bin:$PATH"  
# Prolog  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends gprolog \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
# Scala  
# # with sbt  
ENV SCALA_VERSION="2.12.1"  
ENV SBT_VERSION="0.13.15"  
RUN curl -fsL
"http://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz"
| tar xfz - -C ~ \  
&& mv "$HOME/scala-$SCALA_VERSION" "$HOME/.scala"  
RUN curl -fsL
"http://downloads.typesafe.com/sbt/$SBT_VERSION/sbt-$SBT_VERSION.tgz" | tar
xfz - -C ~ \  
&& mv "$HOME/sbt" "$HOME/.sbt"  
ENV PATH="$HOME/.sbt/bin:$HOME/.scala/bin:$PATH"  
RUN sbt sbtVersion  
# Erlang  
RUN echo "deb http://packages.erlang-solutions.com/debian jessie contrib" >>
/etc/apt/sources.list \  
&& curl -O http://packages.erlang-solutions.com/ubuntu/erlang_solutions.asc \  
&& apt-key add erlang_solutions.asc \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends erlang \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
# Clojure  
# # use Leiningen  
RUN curl -O
https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein \  
&& mv lein /usr/local/bin \  
&& chmod u+x /usr/local/bin/lein  
ENV LEIN_ROOT="1"  
RUN lein  
# Install Haskell  
# # with stack  
RUN echo "deb http://ppa.launchpad.net/hvr/ghc/ubuntu trusty main" >
/etc/apt/sources.list.d/ghc.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys F6F88286 \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends ca-certificates g++ ghc-8.0.2
libtinfo-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
575159689BEFB442 \  
&& echo "deb http://download.fpcomplete.com/debian jessie main" | tee
/etc/apt/sources.list.d/fpco.list \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends stack \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
RUN stack config set system-ghc --global true  
ENV PATH="/opt/ghc/8.0.2/bin:$PATH"  

