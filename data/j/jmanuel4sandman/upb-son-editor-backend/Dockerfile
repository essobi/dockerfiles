FROM pgsandman2016/upb-son-editor-backend-base:v1  
  
#install son-editor-backend  
RUN mkdir -p /root/son-editor/workspaces  
COPY ./nginx.conf /etc/nginx/conf.d/nginx.conf  
COPY . /app  
  
# Set the default directory where CMD will execute  
WORKDIR /app  
  
#set git a dummy user to be enable stashing the config file  
RUN git config user.email "dummy@user.com"  
RUN git config user.name "Dummy User"  
#install the son-editor requirements  
RUN pip install -e .  
  
#expose ports  
#son-editor-backend  
EXPOSE 5000  
#github-webhook  
EXPOSE 5050  
  
#make sure entrypoint is executable  
RUN chmod +x entrypoint.sh  
  
ENTRYPOINT ["./entrypoint.sh"]  

