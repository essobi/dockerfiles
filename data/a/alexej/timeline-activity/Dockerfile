FROM ubuntu  
  
RUN apt-get update \  
&& apt-get install -y wget \  
&& wget https://activitytimeline.com/deployments/activitytimeline-v4.1g.tar.gz
-O /tmp/activitytimeline-v4.1g.tar.gz \  
&& mkdir /data \  
&& tar -C /data -xvf /tmp/activitytimeline-v4.1g.tar.gz  
  
EXPOSE 8040  
CMD /data/activitytimeline/bin/startup.sh && tail -F
/data/activitytimeline/logs/catalina.out

