# Informa qual imagem será gerada a nova imagem  
FROM alpine  
  
MAINTAINER Charles Silva <suporte@charlessilva.com.br>  
  
# Instrução para execultar um arquivo  
RUN apk add --update tar build-base && \  
wget -qO noip.tar.gz http://www.noip.com/client/linux/noip-duc-linux.tar.gz &&
\  
mkdir noip && tar -C noip --strip-components=1 -xvf ./noip.tar.gz && \  
cd noip && sed -i '/no-ip2/d' Makefile && make install && \  
rm -rf /var/cache/apk/* && rm ../noip.tar.gz  
# Informa qual comando será executado quando um container for iniciado  
CMD noip2; while pgrep noip > -; do echo "O processo está em execução"; sleep
5; done; echo "No-ip parou"; exit 1  

