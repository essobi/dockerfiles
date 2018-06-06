FROM steeef/go-rundeck  
MAINTAINER Stephen Price <stephen@stp5.net>  
  
RUN apk --update add bash jq  
RUN mkdir /bundle  
WORKDIR /bundle  
COPY rundeck.sh /bundle/  
RUN chmod +x /bundle/rundeck.sh  
RUN ln -s /bundle/rundeck.sh /bundle/list \  
&& ln -s /bundle/rundeck.sh /bundle/run \  
&& ln -s /bundle/rundeck.sh /bundle/history  

