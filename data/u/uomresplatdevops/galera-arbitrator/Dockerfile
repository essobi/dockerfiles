FROM uomresplatdevops/galera-common  
MAINTAINER Tim Dettrick <t.dettrick@uq.edu.au>  
  
RUN apt-get install -y galera-arbitrator-3  
  
EXPOSE 3306 4444 4567  
ENTRYPOINT ["/usr/bin/garbd"]  

