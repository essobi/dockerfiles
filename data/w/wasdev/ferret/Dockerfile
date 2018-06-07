FROM websphere-liberty  
  
# Install curl and then clean up after (Healthcheck uses curl)  
RUN apt-get update \  
&& apt-get install -y curl \  
&& rm -rf /var/lib/apt/lists/*  
  
# Pull in the ferret WAR  
ENV FERRET_VERSION 1.2  
RUN wget
http://search.maven.org/remotecontent?filepath=net/wasdev/wlp/sample/ferret/$FERRET_VERSION/ferret-$FERRET_VERSION.war
-O /config/dropins/ferret.war  
  
# Add healthcheck file to call then set it as the healthcheck  
ADD healthcheck /opt/ibm/docker  
HEALTHCHECK CMD /opt/ibm/docker/healthcheck  

