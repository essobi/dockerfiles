FROM ubuntu:12.04  
  
COPY . /src  
  
RUN cd /src && apt-get update && apt-get install -y python-dev && apt-get
install -y libmysqlclient-dev && apt-get install -y python-pip && pip install
-r requirements.txt  
  
EXPOSE 8000  
  
CMD cd /src && trac-admin main initenv bloodhound $DATABASE_URL
\--inherit=base.ini && trac-admin main wiki upgrade && trac-admin main
permission add admin TRAC_ADMIN && tracd \--port=$PORT \--basic-
auth="main,.htpasswd,bloodhound" main  

