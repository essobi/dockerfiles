FROM perl:latest  
  
#RUN apt-get update && apt-get -y install vim  
RUN git clone https://github.com/oleg-fiksel/perl_xmas && ln -s
`pwd`/perl_xmas/perl_xmas.pl /usr/local/bin/xmas  
#RUN apt-get clean  
CMD /usr/local/bin/xmas  

