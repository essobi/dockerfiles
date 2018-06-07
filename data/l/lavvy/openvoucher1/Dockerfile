FROM tutum/lamp:latest  
RUN rm -fr /app # && git clone #https://github.com/litzinetz-
de/OpenVoucher.git /app  
COPY ./src /app  
#COPY ./database /var/lib/mysql  
EXPOSE 80 3306  
CMD ["/run.sh"]  
  
# ok do it this way directly  
#RUN mysql -uroot -e "CREATE USER 'openvoucher'@'%' IDENTIFIED BY
'openvoucher'" && \  
# sleep 5 && \  
#mysql -uroot -e "GRANT ALL PRIVILEGES ON *.* TO 'openvoucher'@'%' WITH GRANT
OPTION" && \  
#mysql -uopenvoucher -popenvoucher </app/OpenVoucher/database/tables.sql  
# set up mysql db and tables  
ADD rundb.sh /rundb.sh  
RUN chmod 755 /*.sh  
CMD ["/rundb.sh"]  

