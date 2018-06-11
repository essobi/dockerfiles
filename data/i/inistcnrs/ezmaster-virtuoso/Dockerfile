FROM tenforce/virtuoso:1.2.0-virtuoso7.2.4  
# ----------------------------------------------- #  
# ezMaster configuration #  
# ----------------------------------------------- #  
EXPOSE 8890  
RUN echo '{ \  
"httpPort": 8890, \  
"dataPath": "/data", \  
"configPath": "/tmp/config.json" \  
}' > /etc/ezmaster.json  
# ----------------------------------------------- #  
# Replace tenforce's script (modified loading)  
ADD virtuoso.sh /virtuoso.sh  
ADD config2ini.py /config2ini.py  

