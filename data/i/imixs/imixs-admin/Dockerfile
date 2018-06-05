FROM imixs/wildfly:latest  
  
# Deploy imixs-amdin artefact from latest Github Release  
RUN wget https://github.com/imixs/imixs-admin/releases/download/4.2.3/imixs-
admin-4.2.3.war \  
&& mv imixs-admin-4.2.3.war $WILDFLY_DEPLOYMENT

