FROM debian:jessie  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y \  
git nodejs npm libffi-dev libpq-dev locales \  
python3 python3-setuptools  
RUN easy_install3 pip wheel virtualenv  
RUN ln -s $(which nodejs) /usr/bin/node  
  
RUN echo 'en_AU.UTF-8 UTF-8' > /etc/locale.gen && locale-gen && update-locale
LANG=en_AU.UTF-8  
ENV LANG en_AU.UTF-8  
RUN mkdir -p /code/data  
WORKDIR /code  
  
ADD package.json /code/package.json  
ADD bower.json /code/bower.json  
ADD _deps_html.sh /code/_deps_html.sh  
RUN ./_deps_html.sh  
ADD _deps_collectstatic.sh /code/_deps_collectstatic.sh  
RUN ./_deps_collectstatic.sh  
  
RUN apt-get install -y python3-dev  
ENV WHEELS_ONLY=1  
ADD requirements.txt /code/requirements.txt  
ADD test-requirements.txt /code/test-requirements.txt  
ADD _deps_python.sh /code/_deps_python.sh  
RUN ./_deps_python.sh  
  
ADD manage.py /code/manage.py  
ADD dockci /code/dockci  
ADD tests /code/tests  
ADD pylint.conf /code/pylint.conf  
ADD alembic /code/alembic  
  
EXPOSE 5000  
ENTRYPOINT ["/code/python_env/bin/python" , "/code/manage.py"]  
CMD ["run"]  

