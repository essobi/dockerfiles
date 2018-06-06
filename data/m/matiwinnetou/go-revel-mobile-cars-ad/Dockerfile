FROM google/golang  
MAINTAINER Mateusz Szczap <mati@sz.home.pl>  
RUN go get github.com/revel/cmd/revel  
RUN mkdir -p $GOPATH/src/github.com/matiwinnetou  
RUN cd $GOPATH/src/github.com/matiwinnetou/; git clone
https://github.com/matiwinnetou/go-revel-mobile-cars-adstream.git  
WORKDIR $GOPATH  
EXPOSE 9000  
RUN revel package github.com/matiwinnetou/go-revel-mobile-cars-adstream  
RUN tar xvf go-revel-mobile-cars-adstream.tar.gz  
CMD ./run.sh  

