# Dockerfile for creating BaasBox image with mock data script  
FROM java:8  
MAINTAINER Ruben Laube-Pohto  
  
RUN apt-get update && \  
apt-get install -y bc  
  
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
ADD ./scripts/ /usr/src/baasbox/scripts  
RUN chmod +x ./start  
RUN chmod +x ./scripts/generate_mock_data.sh  
RUN chmod +x ./scripts/start.sh  
RUN chmod +x ./scripts/data.sh  
  
# Expose the default port of BaasBox  
EXPOSE 9000  
CMD ["/usr/src/baasbox/scripts/start.sh"]  
  

