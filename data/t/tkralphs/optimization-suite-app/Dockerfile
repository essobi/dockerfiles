FROM ubuntu:latest  
MAINTAINER Ted Ralphs <ted@lehigh.edu>  
  
RUN apt-get update  
RUN apt-get -y install git subversion gcc clang cmake wget gfortran  
RUN apt-get -y install golang  
  
RUN cd /var  
RUN svn checkout --non-interactive --trust-server-cert https://projects.coin-
or.org/svn/CoinBinary/OptimizationSuite/stable/1.8 /var/optimization-suite  
RUN cd /var/optimization-suite && ./get.AllThirdParty  
RUN cd /var/optimization-suite && ./configure COIN_SKIP_PROJECTS=FlopCpp
--enable-gnu-packages --with-gmpl && make -j4 && make install  
  
ADD webapp /go/solver  
ENTRYPOINT /go/solver/entry.sh  
  
EXPOSE 9090

