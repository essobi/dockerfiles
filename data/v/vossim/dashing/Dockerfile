FROM vossim/dashing  
  
RUN cd /opt/dashboard \  
&& dashing install d5ece60f3e1b909a671d \  
&& dashing install 1d2c1794fba362fd091e # Installing jenkins and jira burn
down widget  
  
ADD extra_files /opt/dashboard/  
  
CMD cd /opt/dashboard && dashing start -p 80  

