FROM imega/base-builder:1.1.0  
COPY . /  
  
RUN apk add --update unzip && \  
rm -rf /var/cache/apk/*  
  
CMD ["/entry.sh"]  

