# Take from official rethinkdb  
FROM rethinkdb  
  
# Update and install python & rethinkdb-driver  
RUN apt-get clean && apt-get update \  
&& apt-get install -y python-pip \  
&& pip install rethinkdb \  
&& apt-get clean  

