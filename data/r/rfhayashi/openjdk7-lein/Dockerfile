FROM rfhayashi/openjdk7-ruby  
  
ENV LEIN_ROOT true  
  
RUN wget -q -O /usr/bin/lein \  
https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein \  
&& chmod +x /usr/bin/lein && lein upgrade 2.6.1

