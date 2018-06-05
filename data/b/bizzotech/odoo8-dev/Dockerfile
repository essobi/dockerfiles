FROM odoo:8  
  
USER root  
  
RUN apt-get update && apt-get install -y gcc python-dev libffi-dev libssl-dev
build-essential  
  
RUN pip install --upgrade setuptools  
RUN pip install oauthlib boto pysftp simplejson  
RUN pip install requests --upgrade  
  
USER odoo  

