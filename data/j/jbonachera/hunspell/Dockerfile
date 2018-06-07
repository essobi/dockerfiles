FROM alpine  
RUN apk -U add hunspell unzip curl && rm -rf /var/cache/apk/* && \  
curl -L http://www.dicollecte.org/download/fr/hunspell-french-
dictionaries-v6.0.2.zip -o /var/tmp/dict.zip && \  
mkdir /usr/share/hunspell/ && cd /usr/share/hunspell/ && unzip
/var/tmp/dict.zip && rm -f /var/tmp/dict.zip && \  
apk del unzip curl && \  
ln -sf /usr/share/hunspell/fr-moderne.aff /usr/share/hunspell/fr.aff && \  
ln -sf /usr/share/hunspell/fr-moderne.dic /usr/share/hunspell/fr.dic  
ENTRYPOINT ["/usr/bin/hunspell"]  

