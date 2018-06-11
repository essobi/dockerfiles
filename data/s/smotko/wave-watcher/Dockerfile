FROM python:2.7  
WORKDIR /code  
ADD requirements.txt /code/  
RUN pip install -r requirements.txt  
ADD . /code/  
ENV PYTHONPATH=.:src/  
ENV PATH=$PATH:bin/  
ENV WW_DEBUG=true  
RUN run_tests  
CMD run_web  

