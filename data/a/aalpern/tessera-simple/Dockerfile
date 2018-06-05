from nodesource/node:precise  
maintainer Adam Alpern <adam.alpern@gmail.com>  
  
run apt-get -y update  
run apt-get -y install python-pip python-dev curl git gunicorn supervisor  
run pip install virtualenv  
  
# Tessera  
add ./config.py /var/lib/tessera/config.py  
  
run mkdir /src  
run git clone https://github.com/aalpern/tessera.git /src/tessera  
workdir /src/tessera  
run script/setup  
workdir /src/tessera/tessera-server  
run ../script/server & sleep 5 && . env/bin/activate && invoke json.import
'../demo/*.json'  
  
# Supervisord  
add ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
expose :80  
cmd ["/usr/bin/supervisord"]  

