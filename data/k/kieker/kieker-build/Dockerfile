FROM openjdk:8-jdk-slim  
  
WORKDIR /opt  
  
# Workaround for https://github.com/docker-library/openjdk/issues/117  
#RUN echo "jdk.tls.disabledAlgorithms=SSLv3, MD2, MD5, MD5withRSA, RSA keySize
< 1024, DSA keySize < 1024, EC keySize < 224, ECDSA" >>
/usr/lib/jvm/java-7-openjdk-amd64/jre/lib/security/java.security  
  
RUN apt-get update -qq && \  
apt-get install -y ca-certificates git r-base r-cran-rserve texlive texlive-
generic-extra texlive-fonts-extra texlive-latex-extra biber --no-install-
recommends && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  

