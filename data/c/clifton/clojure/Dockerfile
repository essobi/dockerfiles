FROM clifton/oracle-java8  
  
ENV LEIN_ROOT true  
  
RUN curl https://raw.github.com/technomancy/leiningen/stable/bin/lein \  
> /usr/local/bin/lein && chmod 755 /usr/local/bin/lein && lein version  
  
EXEC ["lein", "repl"]  

