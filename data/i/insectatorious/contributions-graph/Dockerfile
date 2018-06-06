FROM ubuntu:16.04  
MAINTAINER Sumanas Sarma <insectatorious+docker@gmail.com>  
  
RUN apt-get update  
  
RUN apt-get install -y \  
# Need this to use apt-add-repository - TODO: Add ppa to sources.list manually  
software-properties-common \  
# Need this for `gem install`  
build-essential \  
git  
  
# Install Ruby (needed for SASS)  
RUN apt-add-repository ppa:brightbox/ruby-ng && \  
apt-get update && \  
apt-get install -y \  
ruby2.4 \  
ruby2.4-dev  
  
# Install SASS  
RUN gem install sass  
  
# Install Python and Pip  
RUN apt-get install -y \  
python \  
python-dev \  
python-pip  
  
# Upgrade Pip  
RUN pip install --upgrade pip  
  
# Install Flask: http://flask.pocoo.org/  
# Gunicorn: http://gunicorn.org/  
RUN pip install \  
Flask==0.12.2 \  
gunicorn==19.7.1  
  
WORKDIR /usr/src/app  
  
# Get the contributions graph library  
RUN git clone https://github.com/insectatorious/contributions-graph.git  
WORKDIR contributions-graph  
  
# Get the env ready  
RUN git checkout f1d0e49e3cea80fb8ae24c461a561e01d0314aba && \  
pip install -r requirements.txt && \  
sass --scss contributions/static/style.scss:contributions/static/style.css  
  
COPY ./app.py app.py  
ENV FLASK_APP app.py  
  
CMD ["gunicorn", \  
"-b", \  
"0.0.0.0:5000", \  
"app:app"]

