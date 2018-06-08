FROM skegio/base  
  
RUN apt-get update && apt-get install openjdk-8-jre-headless -y  
RUN curl -fsSL
https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein > \  
/usr/local/bin/lein && \  
chmod 0755 /usr/local/bin/lein  
RUN curl -fsSL https://github.com/boot-clj/boot-
bin/releases/download/latest/boot.sh > \  
/usr/local/bin/boot && \  
chmod 0755 /usr/local/bin/boot  
RUN apt-get install rlwrap -y  

