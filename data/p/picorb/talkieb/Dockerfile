FROM correl/erlang  
  
WORKDIR /app  
ADD ./chat /app  
RUN make all  
  
EXPOSE 6667  
CMD ["sh", "./start.sh"]  

