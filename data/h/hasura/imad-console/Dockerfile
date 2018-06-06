FROM hasura/imad-console:1.2  
#Add all source code  
ADD app /app/  
RUN cd /app && npm run build  
  
#Default command  
CMD ["/app/runserver.sh"]  

