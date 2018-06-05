FROM gliderlabs/herokuish:latest  
  
ONBUILD ADD src /app  
ONBUILD RUN /bin/herokuish buildpack build  
  
ENV PORT=8080  
CMD ["/start", "web"]  
  
EXPOSE 8080  

