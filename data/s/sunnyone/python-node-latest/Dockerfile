# Dockerfile for container with latest Python 3 and Node.js installed  
FROM python:slim  
LABEL "maintainer"="Vadym S. Khondar <vadym@khondar.name>"  
LABEL "description"="Container with latest Python 3 and Node.js"  
  
ARG RUN_PYTHON=1  
ENV RUN_PYTHON=${RUN_PYTHON}  
  
RUN apt-get update && \  
apt-get install -y curl git && \  
curl -sL https://deb.nodesource.com/setup_9.x | /bin/bash - && \  
apt-get install -y nodejs build-essential libmysqlclient-dev && \  
pip install mysqlclient && \  
apt-get purge -y build-essential && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
CMD [ $RUN_PYTHON = 1 ] && python3 || node  
  
# end  

