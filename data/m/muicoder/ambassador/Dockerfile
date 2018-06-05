FROM muicoder/glibc  
  
RUN apk add --no-cache socat && \  
curl -fsSL github.com/muicoder/ambassador/raw/master/run.sh -o
/usr/local/bin/run.sh && chmod +x /usr/local/bin/run.sh  
  
CMD ["run.sh"]  

