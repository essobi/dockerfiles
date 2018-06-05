FROM ytnobody/mecab-psgi  
MAINTAINER ytnobody <ytnobody@gmail.com>  
  
RUN mkdir /root/atom  
  
WORKDIR /root/atom  
RUN cpanm Acme::Shukugawa::Atom JSON  
ADD app.psgi /root/atom/app.psgi  
  

