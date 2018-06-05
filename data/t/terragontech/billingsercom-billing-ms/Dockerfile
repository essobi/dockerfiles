FROM terragontech/python  
WORKDIR /billing_service  
ADD . /billing_service  
CMD chmod +x billing_service/run.sh  
RUN pip install -r billing_service/requirements.txt  
CMD sh billing_service/run.sh  

