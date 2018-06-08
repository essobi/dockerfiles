FROM docker/compose:1.8.0  
  
RUN apk update \  
&& apk upgrade \  
&& apk add ruby docker bash  
  
RUN mkdir /config  
  
ADD nginx.conf /  
ADD cloud.yaml.erb /  
ADD generate-config.rb /  
ADD run.sh /  
  
ENTRYPOINT /run.sh  

