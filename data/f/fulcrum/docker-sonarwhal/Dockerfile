FROM node  
  
#https://github.com/sonarwhal/sonarwhal  
# https://github.com/sonarwhal/sonarwhal/issues/600  
RUN apt-get update && apt-get install -y curl apt-transport-https && \  
npm install -g --engine-strict sonarwhal --unsafe-perm=true  
  
COPY dot-sonarwhalrc /.sonarwhalrc  
  
ENTRYPOINT ["sonarwhal"]  
CMD ["-h"]  
  
# docker build -t sw .  
# docker run sw https://example.com  

