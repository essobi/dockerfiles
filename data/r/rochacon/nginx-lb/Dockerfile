FROM nginx  
RUN apt-get update && apt-get install -yq python python-pip procps && apt-get
clean  
RUN pip install -U pip  
RUN pip install -U docker-py==1.3.1 jinja2==2.8  
COPY nginx-lb-monitor /usr/local/bin/nginx-lb-monitor  
COPY nginx-lb-init /usr/local/bin/nginx-lb-init  
ENTRYPOINT ["/usr/local/bin/nginx-lb-init"]  

