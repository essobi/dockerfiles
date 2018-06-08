FROM python:3.6  
WORKDIR /response_operations_ui  
COPY . /response_operations_ui  
EXPOSE 8085  
RUN pip3 install pipenv && pipenv install --deploy --system  
  
ENTRYPOINT ["python3"]  
CMD ["run.py"]  

