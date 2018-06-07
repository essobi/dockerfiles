# Alpine based stockfish container  
# https://github.com/official-stockfish/Stockfish  
#  
FROM bitnami/minideb:stretch  
  
LABEL maintainer "Kayvan Sylvan <kayvansylvan@gmail.com>"  
  
ENV SOURCE_REPO https://github.com/official-stockfish/Stockfish  
ENV VERSION master  
  
ADD ${SOURCE_REPO}/archive/${VERSION}.tar.gz /root  
WORKDIR /root  
  
RUN if [ ! -d Stockfish-${VERSION} ]; then tar xvzf *.tar.gz; fi \  
&& cd Stockfish-${VERSION}/src \  
&& install_packages make g++ \  
&& make build ARCH=x86-64-modern \  
&& make install \  
&& cd ../.. && rm -rf Stockfish-${VERSION} *.tar.gz  
  
ENTRYPOINT [ "/usr/local/bin/stockfish" ]  

