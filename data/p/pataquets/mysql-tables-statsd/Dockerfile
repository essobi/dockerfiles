FROM pataquets/sql-query-output-to-statsd  
  
ADD ./default.conf /etc/sql-query-output-to-statsd/  
ADD ./queries.csv /etc/sql-query-output-to-statsd/  
  
CMD [ "/etc/sql-query-output-to-statsd/default.conf" ]  

