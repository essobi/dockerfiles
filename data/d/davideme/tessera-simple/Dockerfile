FROM nodesource/node:precise  
  
RUN apt-get update  
RUN apt-get install -y python-pip python-dev curl git gunicorn supervisor  
  
# Tessera  
RUN mkdir /src && git clone https://github.com/urbanairship/tessera.git
/src/tessera  
ADD config.py /src/tessera/tessera/config.py  
  
workdir /src/tessera  
RUN pip install -r requirements.txt  
RUN pip install -r dev-requirements.txt  
RUN npm install -g grunt-cli  
RUN npm install  
RUN grunt  
RUN mkdir -p /var/lib/tessera/  
  
RUN invoke db.init  
RUN invoke run & sleep 5 && invoke json.import 'demo/*.json'  
  
# Supervisord  
ADD ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
#Bash script  
ADD ./init_and_start.sh /src/tessera/init_and_start.sh  
RUN chmod ugo+x /src/tessera/init_and_start.sh  
  
expose :80  
CMD ["/src/tessera/init_and_start.sh"]  

