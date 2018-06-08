FROM ubuntu:16.04  
MAINTAINER Fabio Rehm "fgrehm@gmail.com"  
RUN apt-get update \  
&& apt-get install -y curl \  
&& curl -L 'https://sites.google.com/site/afonsosales/tools/linux64/san-lite-
solver?attredirects=0' > /usr/bin/san-lite-solver \  
&& chmod +x /usr/bin/san-lite-solver  
ENTRYPOINT ["/usr/bin/san-lite-solver"]  

