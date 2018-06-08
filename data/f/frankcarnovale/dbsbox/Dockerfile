FROM wnameless/postgresql-phppgadmin  
  
COPY dbsbox.sh /etc/profile.d  
COPY test_*.sql /sql/  
COPY builder.sh starter.sh /  
  
RUN /builder.sh  
CMD /starter.sh  
  

