FROM ubuntu  
MAINTAINER Steinway Wu "https://github.com/steinwaywhw/docker-ats"  
# for installing erlang/elixir  
WORKDIR /tmp  
RUN apt-get -qq update  
RUN apt-get -qq install -y wget libgmp3-dev libgc-dev make gcc build-essential
git \  
bash libjson-c-dev pkg-config mit-scheme openjdk-8-jdk unzip nodejs  
RUN wget http://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb  
RUN dpkg -i erlang-solutions_1.0_all.deb  
RUN apt-get -qq update  
RUN apt-get -qq install -yq esl-erlang elixir  
RUN apt-get clean  
  
RUN wget
http://repo1.maven.org/maven2/org/clojure/clojure/1.8.0/clojure-1.8.0.zip  
RUN unzip clojure-1.8.0.zip && rm clojure-1.8.0.zip  
RUN echo "export CLASSPATH=\${HOME}/clojure-1.8.0/*:\${CLASSPATH}:" >>
${HOME}/.bashrc  
  
ADD ./install.sh /tmp/install.sh  
RUN chmod +x install.sh && ./install.sh  
  
WORKDIR /root  
ENTRYPOINT /bin/bash  
  

