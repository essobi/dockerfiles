FROM stilliard/pure-ftpd  
  
ENV PUBLICHOST localhost  
  
CMD /run.sh -c 50 -C 50 -l puredb:/etc/pure-ftpd/pureftpd.pdb -E -j -R -P
$PUBLICHOST -p 30000:30099  
  
EXPOSE 21 30000-30099  

