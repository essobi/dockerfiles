FROM ibmcom/swift-ubuntu-runtime:latest  
  
EXPOSE 8080  
  
COPY Server /EasyLoginServer  
RUN chown -R root:root /EasyLoginServer  
RUN chown -R www-data:www-data /EasyLoginServer/.build  
  
USER www-data  
  
ENTRYPOINT [ "/EasyLoginServer/.build/x86_64-unknown-linux/release/EasyLogin"
]  

