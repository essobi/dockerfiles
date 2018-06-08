FROM clojure:lein-alpine  
MAINTAINER David Rolle <david.rolle@gmail.com>  
  
RUN lein new luminus app +datomic +reagent +auth +kibit \  
&& rm -rf ~/.m2 \  
&& cd app && lein deps \  
&& cd .. && rm -rf app  

