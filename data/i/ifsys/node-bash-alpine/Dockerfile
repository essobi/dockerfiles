FROM mhart/alpine-node:9.2  
RUN apk update \  
&& apk --no-cache add bash bash-completion sed \  
&& sed -i -e "s/bin\/ash/bin\/bash/" /etc/passwd \  
&& apk del sed  
  
CMD /bin/bash  

