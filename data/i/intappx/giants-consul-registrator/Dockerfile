# Base image  
FROM gliderlabs/registrator  
  
# Install curl  
RUN apk-install curl  
  
# Run registrator  
ENTRYPOINT /bin/registrator \  
  
# Register the docker0 internal IP (as returned by docker inspect) and port
instead of the host mapped ones  
-internal \  
  
# Resync all registered services this often (in seconds). 0 (default) to
disable  
-resync=5 \  
  
# Backend for registrator to use (consul/etcd/Sky DNS 2):
backend://address:port  
consul://$(curl http://169.254.169.254/latest/meta-data/local-ipv4):8500  

