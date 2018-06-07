FROM emirb/php72:latest  
RUN apt-get update && apt-get install -y ant  
RUN apt-get clean  
RUN groupadd --gid 115 jenkins  
RUN useradd -ms /bin/bash jenkins --uid 110 --gid 115  

