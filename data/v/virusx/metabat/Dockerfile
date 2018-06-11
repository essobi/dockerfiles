FROM alpine  
ENV METABAT_VERSION=2.12.1  
RUN apk add --update wget ca-certificates bash && \  
wget "https://bitbucket.org/berkeleylab/metabat/downloads/metabat-static-
binary-linux-x64_v${METABAT_VERSION}.tar.gz" -O- | tar --no-same-owner -xz &&
\  
mv metabat/* /usr/local/bin/ && \  
rmdir metabat && \  
apk del wget ca-certificates && \  
rm -rf /var/cache/apk/*  

