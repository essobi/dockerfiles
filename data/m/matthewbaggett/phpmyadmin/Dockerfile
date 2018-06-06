FROM yoshz/phpmyadmin  
MAINTAINER Matthew Baggett <matthew@baggett.me>  
ADD startup.sh /startup.sh  
ADD phpmyadmin.sql /phpmyadmin.sql  
RUN chmod 0500 /apache-run.sh  
CMD ["/startup.sh"]  

