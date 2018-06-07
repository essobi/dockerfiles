FROM alpine:3.4  
RUN apk --no-cache add git && \  
rm -rf /var/lib/apt/lists/*  
  
VOLUME /git  
WORKDIR /git  
  
ENTRYPOINT ["git"]  
CMD ["--help"]  

