FROM python:2.7  
WORKDIR /  
RUN pip install -r https://raw.githubusercontent.com/utky/budget-
analyse/master/requirements.txt  
RUN pip install git+https://github.com/utky/budget-analyse.git  
  
ENTRYPOINT ["/usr/local/bin/python"]  
CMD ["-m", "budget"]  

