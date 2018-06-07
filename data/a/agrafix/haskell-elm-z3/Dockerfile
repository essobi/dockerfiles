FROM agrafix/docker-haskell-elm:lts-3.17_20151207  
RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com F6F88286 && \  
echo 'deb http://ppa.launchpad.net/hvr/z3/ubuntu trusty main' >
/etc/apt/sources.list.d/smt.list  
RUN apt-get update -y && apt-get -y install z3=4.4.0-2ubuntu1  
RUN z3 --version  

