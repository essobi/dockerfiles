FROM alpine:3.3  
RUN apk --update upgrade && \  
apk add curl ca-certificates && \  
update-ca-certificates && \  
rm -rf /var/cache/apk/*  
RUN wget -O /usr/local/bin/gdrive
"https://docs.google.com/uc?id=0B3X9GlR6EmbnQ0FtZmJJUXEyRTA&export=download"  
RUN chmod +x /usr/local/bin/gdrive  
ENTRYPOINT ["gdrive"]  

