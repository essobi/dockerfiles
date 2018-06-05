FROM fxtrader/finance-hostedtrader  
MAINTAINER Joao Costa <joaocosta@zonalivre.org>  
  
RUN cpanm --notest Dancer2 Starman MCE  
  
ADD . /webapp  
  
EXPOSE 5000  
CMD ["starman", "/webapp/bin/app.psgi"]  

