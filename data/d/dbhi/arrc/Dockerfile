FROM ubuntu:14.04  
RUN apt-get update -qq  
RUN apt-get install -y python python-dev python-pip python-scipy pkg-config
libfreetype6-dev libpng-dev  
  
# Inline heavy dependencies to use container caching.  
RUN pip install numpy  
RUN pip install scikit-learn  
RUN pip install pandas  
RUN pip install nltk  
  
ADD . /arrc  
WORKDIR /arrc  
  
RUN pip install -r requirements.txt  
  
EXPOSE 5000  
ENTRYPOINT ["python", "rs.py"]  
  
CMD ["0.0.0.0"]  

