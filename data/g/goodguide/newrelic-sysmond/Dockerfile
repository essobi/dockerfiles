FROM quay.io/goodguide/base:ubuntu-16.04  
RUN apt-key adv --keyserver hkp://hkps.pool.sks-keyservers.net --recv-keys
548C16BF \  
&& echo "deb http://apt.newrelic.com/debian/ newrelic non-free" >
/etc/apt/sources.list.d/newrelic.list \  
&& apt-get update \  
&& apt-get install -y \  
newrelic-sysmond \  
curl  
  
ADD ./entrypoint.sh /bin/entrypoint  
ENTRYPOINT ["/bin/entrypoint"]  

