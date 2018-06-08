FROM python:3.5-alpine  
  
RUN apk add --update \  
build-base \  
&& pip install sacredboard \  
&& rm -rf /var/cache/apk/*  
  
EXPOSE 5000  
ENV MONGODB_URL mongodb://localhost?set_your_own  
ENV MONGODB_DATABASE sacred  
  
ENTRYPOINT sacredboard -mu $MONGODB_URL $MONGODB_DATABASE  

