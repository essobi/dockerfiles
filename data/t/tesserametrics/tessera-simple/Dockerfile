from python:2.7  
maintainer Adam Alpern <adam.alpern@gmail.com>  
  
run pip install supervisor  
run pip install tessera  
  
# Tessera  
add ./config.py /var/lib/tessera/config.py  
  
# Supervisord  
run mkdir /var/log/supervisor  
add ./supervisord.conf /etc/supervisord.conf  
  
expose :5000  
cmd ["supervisord"]  

