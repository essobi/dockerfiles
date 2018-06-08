FROM lightjason/agentspeak:latest  
  
# --- configuration section ----------------------  
ENV REST_VERSION HEAD  
  
# --- build section ------------------------------  
RUN git clone https://github.com/LightJason/REST.git /tmp/rest  
RUN cd /tmp/rest && git checkout $REST_VERSION  
RUN cd /tmp/rest && mvn package install  

