FROM alpine:latest  
  
LABEL maintainer Jan Krueger <jkrueger(at)cebitec.uni-bielefeld.de>  
  
#install Krona with dependencies  
RUN apk update && apk add curl wget perl make bash && wget
https://github.com/marbl/Krona/releases/download/v2.7/KronaTools-2.7.tar &&
tar -xvf KronaTools-2.7.tar && rm KronaTools-2.7.tar && cd KronaTools-2.7 &&
./install.pl && rm -rf /var/cache/apk/  
  
#Databases  
RUN KronaTools-2.7/updateTaxonomy.sh  
#RUN KronaTools-2.7/updateAccessions.sh  
# biocontainer conventions  
RUN mkdir /data  
WORKDIR /data  
  

