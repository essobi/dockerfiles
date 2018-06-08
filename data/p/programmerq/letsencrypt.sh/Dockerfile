FROM python:2-alpine  
RUN apk add --no-cache bash git openssl curl  
RUN pip install dns-lexicon  
ADD
https://raw.githubusercontent.com/AnalogJ/lexicon/master/examples/letsencrypt.default.sh
lexicon.letsencrypt.sh  
RUN chmod +x lexicon.letsencrypt.sh  
RUN git clone https://github.com/lukas2511/letsencrypt.sh.git  
WORKDIR /letsencrypt.sh  
ENTRYPOINT ["/letsencrypt.sh/letsencrypt.sh"]  
#RUN ln -sf /certs/domains.txt /domains.txt  

