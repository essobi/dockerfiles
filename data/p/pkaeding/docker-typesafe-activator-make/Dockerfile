FROM andrewrothstein/docker-typesafe-activator  
MAINTAINER patrick@kaeding.name  
  
RUN apt-get update && apt-get install -y make python-pip  
RUN pip install awscli  
  
ENV PATH="/opt/activator/bin:${PATH}"  

