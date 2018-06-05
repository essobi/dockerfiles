# Dockerfile for creating the main BaasBox image  
FROM java:8  
MAINTAINER Ruben Laube-Pohto  
  
RUN mkdir -p /usr/src/  
WORKDIR /usr/src/  
# Download BaasBox. Could not find means of downloading a specific version.  
# Could be predownloaded and COPYed to the image.  
RUN wget --content-disposition http://www.baasbox.com/download/baasbox-
stable.zip  
RUN unzip baasbox*.zip  
RUN rm baasbox*.zip  
RUN mv baasbox-*/ baasbox/  
WORKDIR baasbox/  
RUN chmod +x ./start  
  
# Expose the default port of BaasBox  
EXPOSE 9000  
CMD ["./start"]  

