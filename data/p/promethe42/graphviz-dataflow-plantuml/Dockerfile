FROM alpine:edge  
MAINTAINER Jean-Marc Le Roux <jeanmarc.leroux@gmail.com>  
  
ENV PLANTUML_VERSION=1.2017.16  
ENV LANG C.UTF-8  
RUN apk update && \  
apk add git make  
  
# Graphviz  
RUN apk add graphviz  
  
# Dataflow  
RUN git clone https://github.com/sonyxperiadev/dataflow.git
/usr/local/dataflow/  
WORKDIR /usr/local/dataflow/  
  
RUN apk add cabal ghc libc-dev zlib-dev && \  
cabal update && \  
cabal sandbox init && \  
cabal install --only-dependencies && \  
cabal configure && \  
cabal install && \  
ln -s /usr/local/dataflow/.cabal-sandbox/bin/dataflow /usr/bin/dataflow  
  
# PantUML  
RUN apk add openjdk8-jre ttf-dejavu && \  
wget
"https://downloads.sourceforge.net/project/plantuml/${PLANTUML_VERSION}/plantuml.${PLANTUML_VERSION}.jar"
-O /usr/lib/plantuml.jar  
  
# Cleanup  
RUN rm -rf /tmp/* /var/tmp/*  

