FROM python  
  
WORKDIR /src  
RUN pip install codecov  
  
ENTRYPOINT codecov -t "$CODECOV_TOKEN"  

