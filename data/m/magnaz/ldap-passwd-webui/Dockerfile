FROM python:3.6-alpine3.6  
WORKDIR /opt/ldap-passwd-webui  
  
COPY . .  
  
RUN pip install -r requirements.txt  
  
ENTRYPOINT ["waitress-serve", "app:application"]  
  
EXPOSE 8080  

