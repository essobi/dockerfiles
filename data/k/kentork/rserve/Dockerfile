FROM r-base:3.4.0  
RUN R -q -e "install.packages('Rserve', repos='https://cran.r-project.org')"  
  
ADD Rserv.conf /etc/Rserv.conf  
EXPOSE 6311  
ENTRYPOINT ["R", "CMD", "Rserve.dbg", "--vanilla", "--slave", "--max-
ppsize=100000", "--RS-conf", "/etc/Rserv.conf"]  

