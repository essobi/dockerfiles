FROM kibana:4.1.1  
# Use custom entrypoint shell script  
COPY docker-entrypoint.sh /custom-entrypoint.sh  
RUN chmod +x /custom-entrypoint.sh  
ENTRYPOINT ["/custom-entrypoint.sh"]  
CMD ["kibana"]

