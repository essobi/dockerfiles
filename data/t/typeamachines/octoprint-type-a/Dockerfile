FROM debian:8.4  
RUN apt-get update  
RUN apt-get install -y -q git python-pip python-setuptools python-dev  
RUN git clone https://bitbucket.org/typeamachines/octoprint-type-a.git  
CMD git checkout docker  
WORKDIR /octoprint-type-a  
CMD python setup.py install --user  
EXPOSE 5000  
CMD ./run --iknowwhatimdoing  
  

