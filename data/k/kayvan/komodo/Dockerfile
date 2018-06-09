# Komodo chess engine  
#  
FROM bitnami/minideb:stretch  
  
LABEL maintainer "Kayvan Sylvan <kayvansylvan@gmail.com>"  
  
ENV ZIP_FILE https://komodochess.com/pub/komodo-9.zip  
  
ADD ${ZIP_FILE} /root  
WORKDIR /root  
  
RUN install_packages unzip \  
&& unzip *.zip \  
&& cp */Linux/komodo-*-linux /usr/local/bin/komodo \  
&& rm -f *.zip  
  
ENTRYPOINT [ "/usr/local/bin/komodo" ]  

