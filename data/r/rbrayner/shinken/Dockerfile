FROM rohit01/shinken_thruk_graphite  
  
RUN apt-get update && apt-get upgrade -y && apt-get install -y vim
libreadline-dev libconfig-dev libssl-dev lua5.2 liblua5.2-dev libevent-dev
libjansson-dev python-dev make libffi-dev libssl-dev  
  
RUN pip install passlib  
RUN pip install alignak_backend_client  
RUN pip install twx.botapi  
RUN pip install requests[security]  
  
RUN shinken --init  
RUN shinken install pickle-retention-file-scheduler  
RUN shinken install pickle-retention-file-generic  
RUN touch /var/lib/shinken/retention.dat  
RUN chown shinken.shinken /var/lib/shinken/retention.dat  
RUN chmod 660 /var/lib/shinken/retention.dat  
RUN chown shinken.shinken /var/lib/shinken -R  
RUN chown shinken.shinken /var/log/shinken -R  
RUN chmod 777 /var/log/shinken -R  
  
ENV TZ=America/Recife  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
COPY shinken_apache.conf /etc/apache2/conf.d/  
  
EXPOSE 80 7770  

