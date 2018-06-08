FROM clojure:latest  
MAINTAINER Nicolas Long <nicolaslong@gmail.com>  
  
RUN echo '{:user {:plugins [[lein-ring "0.9.6"]]}}' > /root/.lein/profiles.clj  
  
RUN lein  

