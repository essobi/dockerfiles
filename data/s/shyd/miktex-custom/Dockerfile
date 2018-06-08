FROM shyd/miktex  
  
RUN mkdir /miktex/libraries  
COPY libraries /miktex/libraries  
  
USER root  
  
RUN mpm --install babel-german  
RUN initexmf --admin \--user-roots=/miktex/libraries  
RUN initexmf --admin --update-fndb  
  
USER miktex  

