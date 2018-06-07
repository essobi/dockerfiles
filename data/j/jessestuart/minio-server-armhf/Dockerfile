FROM arm32v7/busybox  
COPY lib/minio /bin/minio  
EXPOSE 9000  
VOLUME ["/export"]  
ENTRYPOINT ["minio"]  

