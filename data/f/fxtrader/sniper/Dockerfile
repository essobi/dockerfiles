FROM fxtrader/scripts  
MAINTAINER Joao Costa <joaocosta@zonalivre.org>  
  
RUN cpanm --notest DateTime::Format::Strptime  
  
ADD bin bin  
  
CMD /root/bin/fx-sniper.pl  

