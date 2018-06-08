FROM relayrides/locust:solo  
  
ENV MASTER_HOST master  
  
CMD if [ -e /locust-tasks/requirements.txt ]; then pip install --no-cache-dir
-r /locust-tasks/requirements.txt; fi \  
&& locust --slave --master-host $MASTER_HOST -f $LOCUST_FILE
\--host=$TARGET_HOST -L $LOGLEVEL  

