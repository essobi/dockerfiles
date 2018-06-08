FROM frolvlad/alpine-glibc  
  
ADD https://github.com/prbinu/tls-scan/releases/download/0.1.6/tls-scan-
linux.tar.gz /tls-scan-linux.tar.gz  
  
RUN echo "029f7d541f4a68318521d28a9d92cc7699ac40a1a68a24f05300a4f9aab4459c
/tls-scan-linux.tar.gz" | sha256sum -c && \  
tar -zxf /tls-scan-linux.tar.gz && \  
rm /tls-scan-linux.tar.gz  
  
USER nobody  
  
WORKDIR /tls-scan  
ENTRYPOINT ["/tls-scan/tls-scan"]  
CMD ["--help"]  

