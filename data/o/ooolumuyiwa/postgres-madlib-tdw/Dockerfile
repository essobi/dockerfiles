FROM ooolumuyiwa/postgres-pgpython-plr-madlib  
ENV PG_MAJOR 9.6  
RUN apt-get update &&\  
apt-get install -y postgresql-plpython3-9.6  
RUN apt-get install -y libsybdb5 freetds-dev freetds-common  
#leave out wget and git install we don't need it  
#commented out code until we can get the tds foreign wrapper working  
#RUN git clone https://github.com/GeoffMontee/tds_fdw.git  
#RUN cd tds_fdw  
#RUN make USE_PGXS=1  
#RUN sudo make USE_PGXS=1 install  
#RUN cd ..  
#data in volume location /var/lib/postgresql/data  
ENTRYPOINT ["/docker-entrypoint.sh"]  
EXPOSE 5432  
CMD ["postgres"]  
  

