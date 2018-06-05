FROM tulios/burrow-stats  
  
ENV DOCKERIZE_VERSION v0.4.0  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
\  
&& rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
COPY ./config /etc/burrow-stats  
  
CMD ["dockerize", \  
"-template", \  
"/etc/burrow-stats/templates/configs.tmpl:/opt/burrow-stats/configs.json", \  
"npm", "start"]  

