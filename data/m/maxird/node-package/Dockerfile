FROM maxird/node-build:7  
ADD bootstrap.sh /app/  
ADD package.sh /app/  
ADD nsp-check-deep.sh /app/  
  
WORKDIR /app  
  
RUN mkdir -p /out && \  
ln -sf /out /app/out  
VOLUME ["/out"]  
  
CMD ["/app/bootstrap.sh"]  

