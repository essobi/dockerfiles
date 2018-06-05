FROM ibhde/bird-lgproxy  
  
EXPOSE 8000  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \  
python-dnspython \  
graphviz \  
python-pydot \  
python-memcache \  
whois  
  
WORKDIR /bird-lg  
  
CMD ["lg:app"]  

