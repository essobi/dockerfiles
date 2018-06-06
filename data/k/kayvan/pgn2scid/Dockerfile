# pgn2scid tool in a container  
#  
# https://github.com/CasualPyDev/pgn2scid in a container  
#  
FROM kayvan/scidvspc:latest  
  
LABEL maintainer "Kayvan Sylvan <kayvansylvan@gmail.com>"  
  
ENV VERSION master  
  
ADD https://github.com/CasualPyDev/pgn2scid/archive/${VERSION}.tar.gz
/home/scid  
  
RUN if [ ! -d pgn2scid-${VERSION} ]; then tar xvzf ${VERSION}.tar.gz; fi \  
&& cd pgn2scid-${VERSION} \  
&& apt-get update \  
&& apt-get -y install python3 python3-tk \  
&& cp pgn2scid*.pyw /usr/local/bin/pgn2scid \  
&& chmod +x /usr/local/bin/pgn2scid && cd .. \  
&& rm -rf /var/lib/apt/lists/* pgn2scid-*/ ${VERSION}.tar.gz  
  
ENTRYPOINT ["/usr/local/bin/pgn2scid"]  

