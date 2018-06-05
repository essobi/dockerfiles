FROM alpine:3.5  
# Install OpenSSL  
RUN apk --no-cache add openssl  
  
# Add gost support into OpenSSL configuration file  
RUN sed -i '5i' /etc/ssl/openssl.cnf  
RUN sed -i '6i openssl_conf=openssl_def' /etc/ssl/openssl.cnf  
RUN sed -i '7i' /etc/ssl/openssl.cnf  
RUN echo "" >> /etc/ssl/openssl.cnf  
RUN echo "# OpenSSL default section" >> /etc/ssl/openssl.cnf  
RUN echo "[openssl_def]" >> /etc/ssl/openssl.cnf  
RUN echo "engines = engine_section" >> /etc/ssl/openssl.cnf  
RUN echo "" >> /etc/ssl/openssl.cnf  
RUN echo "# Engine scetion" >> /etc/ssl/openssl.cnf  
RUN echo "[engine_section]" >> /etc/ssl/openssl.cnf  
RUN echo "gost = gost_section" >> /etc/ssl/openssl.cnf  
RUN echo "" >> /etc/ssl/openssl.cnf  
RUN echo "# Engine gost section" >> /etc/ssl/openssl.cnf  
RUN echo "[gost_section]" >> /etc/ssl/openssl.cnf  
RUN echo "engine_id = gost" >> /etc/ssl/openssl.cnf  
RUN echo "dynamic_path = /usr/lib/engines/libgost.so" >> /etc/ssl/openssl.cnf  
RUN echo "default_algorithms = ALL" >> /etc/ssl/openssl.cnf  
RUN echo "CRYPT_PARAMS = id-Gost28147-89-CryptoPro-A-ParamSet" >>
/etc/ssl/openssl.cnf  

