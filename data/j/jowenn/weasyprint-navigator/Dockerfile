FROM python:3-stretch  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install build-
essential python3-dev python3-pip python3-cffi libcairo2 libpango-1.0-0
libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info  
RUN pip install WeasyPrint  
RUN perl -p -i -e "s/127.0.0.1/0.0.0.0/" /usr/local/lib/python3.6/site-
packages/weasyprint/navigator.py  
  
EXPOSE 5000  
CMD ["python", "-m" , "weasyprint.navigator"]  

