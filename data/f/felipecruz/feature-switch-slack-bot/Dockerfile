# Create a minimal container to run a Golang static binary  
FROM centurylink/ca-certs  
MAINTAINER Felipe Cruz "felipecruz91@hotmail.es"  
#EXPOSE 8080  
WORKDIR /app  
  
# copy binary into image  
COPY app /app/  
  
ENTRYPOINT ["./app"]

