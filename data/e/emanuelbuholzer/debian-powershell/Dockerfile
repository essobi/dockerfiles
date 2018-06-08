# Set debian as the base image  
FROM debian:latest  
  
# Apply metadata  
LABEL com.emanuelbuholzer.is-beta=true \  
com.emanuelbuholzer.is-production=false \  
com.emanuelbuholzer.version="0.0.1-beta"  
  
# Install curl and https transport handlers for apt  
# Note: The official Debian image automatically cleans up the apt cache by
removing /var/lib/apt/lists
(https://github.com/moby/moby/blob/03e2923e42446dbb830c654d0eec323a0b4ef02a/contrib/mkimage/debootstrap#L82-L105)  
RUN apt-get update && apt-get install -y apt-transport-https curl  
  
# Import the public repository GPG keys  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -  
  
# Regdister the microsoft repository  
RUN curl https://packages.microsoft.com/config/ubuntu/14.04/prod.list | tee
/etc/apt/sources.list.d/microsoft.list  
  
# Install powershell  
RUN apt-get update && apt-get install -y powershell  
  
# Set powershell as the entrypoint  
ENTRYPOINT ["powershell"]  

