FROM ubuntu:17.04  
  
ENV LC_ALL C.UTF-8  
ENV LANG C.UTF-8  
ENV PYTHONDONTWRITEBYTECODE 1  
  
RUN apt-get update  
RUN apt-get install --yes --no-install-recommends \  
python3.6 python3-pip python3-setuptools  
RUN pip3 install --upgrade pip  
RUN pip3 install pipenv  
  
RUN useradd -ms /bin/bash showsparker  
  
ADD Pipfile /home/showsparker/showsparker_api/  
ADD Pipfile.lock /home/showsparker/showsparker_api/  
RUN chown -R showsparker. /home/showsparker/  
  
USER showsparker  
WORKDIR /home/showsparker/showsparker_api/  
  
RUN pipenv install --ignore-hashes --python /usr/bin/python3.6  
  
ADD . /home/showsparker/showsparker_api/  
USER root  
RUN chown -R showsparker. /home/showsparker/  
USER showsparker  
  
EXPOSE 8000  
CMD ["pipenv", "run", "gunicorn", "--bind", "0.0.0.0:8000",
"showsparker_api.wsgi"]  

