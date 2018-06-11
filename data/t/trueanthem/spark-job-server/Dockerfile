  
FROM trueanthem/mesos  
  
# Don't care about the all the mesos crap that was installed for mesos. We
only want the native lib  
RUN find / -name \\*mesos\\* | perl -ne 'print if !/mesos(.*)\\.(so|la|jar)/'
| xargs rm -rf  
  
# Download the pre-built package  
RUN mkdir -p /job-server && \  
cd /job-server && \  
wget -qO- https://github.com/nextglass/spark-
jobserver/raw/jobserver-0.5.1-BUILD-4.28.2015/dist/job-server.tar.gz | tar xz  
  
ADD run.sh /job-server/  
ADD compute-classpath.sh /spark/bin/  
COPY local.conf.template /job-server/production.conf  
WORKDIR /job-server  
  
ENTRYPOINT ["/job-server/run.sh"]  

