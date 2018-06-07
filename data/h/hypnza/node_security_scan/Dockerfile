FROM mhart/alpine-node  
  
# ensure script changes break cache, in case newer version of modules were
installed  
COPY scan.sh /tmp  
RUN chmod +x /tmp/scan.sh  
  
RUN npm install -g snyk nsp  
  
CMD /tmp/scan.sh  

