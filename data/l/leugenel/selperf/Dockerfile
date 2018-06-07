FROM selenium/standalone-firefox-debug:2.53.0  
COPY perf.jar /home/perf.jar  
COPY docker-entrypoint.sh /home/docker-entrypoint.sh  
RUN ["chmod", "+x", "/home/docker-entrypoint.sh"]  
CMD /home/docker-entrypoint.sh  

