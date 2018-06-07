FROM alpine:latest  
  
LABEL author="Jat <chat@jat.email>"  
LABEL version="0.0.3"  
  
COPY IntelliJIDEALicenseServer /usr/local/bin  
  
EXPOSE 8017  
ENTRYPOINT ["/usr/local/bin/IntelliJIDEALicenseServer"]  
CMD ["-p", "8017", "-u", "SinoSky"]  

