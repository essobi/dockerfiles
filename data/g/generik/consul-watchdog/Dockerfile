FROM python:2-onbuild  
ENV CONSUL_ENPOINT http://172.17.42.1:8500  
ENV REGION eu-west-1  
ENV WATCHDOG_OPTS "--dryrun --debug"  
RUN mkdir -p /service  
WORKDIR /service  
  
ADD consul-watchdog /service/  
ADD get-stack-instances.py /service/  
ADD run.sh /service/  
  
CMD /service/run.sh  

