FROM java:8  
RUN apt-get update  
  
RUN apt-get install -y unzip rlwrap  
  
ADD
http://central.maven.org/maven2/org/clojure/clojure/1.6.0/clojure-1.6.0.zip
clojure.zip  
  
RUN unzip clojure.zip  
  
ADD clj /bin/clj  
ADD clj_completions /.clj_completions  
ADD start /start  
  
ADD https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein
/bin/lein  
RUN chmod a+x /bin/lein  
  
RUN lein self-install  
  
CMD ["clj"]  

