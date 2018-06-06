ARG from_image=couchbase:community  
  
FROM ${from_image}  
  
ADD setup.sh /bin/start-cb.sh  
  
HEALTHCHECK \--interval=5s --timeout=1s CMD test "$( cat /tmp/status )" =
"ready"  
ENTRYPOINT ["bash", "/bin/start-cb.sh"]  

