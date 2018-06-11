FROM debian  
  
RUN apt-get update && apt-get install polipo curl -y && apt-get clean  
USER proxy  
ENV PARENT_PROXY localhost:1080  
EXPOSE 8123  
CMD polipo proxyAddress="::0" socksParentProxy="$PARENT_PROXY"

