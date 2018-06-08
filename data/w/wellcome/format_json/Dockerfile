FROM wellcome/python3  
  
LABEL maintainer "Wellcome <wellcomedigitalplatform@wellcome.ac.uk>"  
LABEL description "A Docker image for formatting JSON"  
  
COPY format_json.py /format_json.py  
  
VOLUME /repo  
WORKDIR /repo  
  
ENTRYPOINT ["python3", "/format_json.py"]

