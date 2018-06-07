FROM latera/activiti:5.19.0  
COPY assets /assets/  
COPY ./*.sh /  
RUN apt-get update \  
&& apt-get install -y zip \  
git \  
postgresql-client  
  
# download and deploy Latera Activiti Extension Pack  
WORKDIR /tmp  
RUN wget https://github.com/latera/activiti-
ext/releases/download/v1.0/activiti-latera-1.0-full.zip  
RUN unzip activiti-latera-1.0-full.zip  
RUN cp activiti-latera-1.0-full/* $CATALINA_HOME/webapps/activiti-
explorer/WEB-INF/lib/ \  
&& cp activiti-latera-1.0-full/* $CATALINA_HOME/webapps/activiti-rest/WEB-
INF/lib/  
# download HydraOMS demo processes  
RUN rm -rf /tmp/*  
WORKDIR /opt  
RUN git clone https://github.com/latera/activiti-homs-demo.git  
  
ENTRYPOINT ["/entrypoint_ah.sh"]  

