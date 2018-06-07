FROM tomsaleeba/natcap-invest-docker:3.4.2-pollination  
  
ADD docker/ requirements.txt /app/  
ADD natcap_invest_docker_flask/ /app/natcap_invest_docker_flask/  
WORKDIR /app/  
RUN /bin/bash setup.sh  
ENTRYPOINT [ "/bin/bash", "run.sh" ]  

