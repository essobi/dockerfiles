FROM python:latest  
MAINTAINER vsochat@stanford.edu  
  
RUN apt-get update  
RUN apt-get -y install build-essential  
RUN apt-get -y install apt-utils  
RUN apt-get -y install cmake  
RUN apt-get -y install wget  
RUN apt-get -y install unzip  
RUN apt-get -y install python-tk  
RUN apt-get -y install python-dev  
RUN apt-get -y install pkg-config  
RUN apt-get -y install libffi-dev  
RUN apt-get -y install libssl-dev  
RUN apt-get -y install qt-sdk  
RUN apt-get -y install libtool \  
autotools-dev \  
automake \  
autoconf \  
git  
  
# Software dependencies.  
# This is equivalent of requirements.txt, run on image build  
RUN pip install --upgrade pip  
RUN pip install cycler==0.10.0  
RUN pip install h5py==2.6.0  
RUN pip install matplotlib==1.5.3  
RUN pip install nose==1.3.7  
RUN pip install numpy==1.11.0  
RUN pip install pandas==0.18.1  
RUN pip install Pillow==3.2.0  
RUN pip install pydicom==0.9.9  
RUN pip install pyparsing==2.1.10  
RUN pip install python-dateutil==2.5.3  
RUN pip install pytz==2016.4  
RUN pip install runcython==0.2.5  
RUN pip install scipy==0.18.1  
RUN pip install six==1.10.0  
RUN pip install simplejson  
  
# Dependencies for simple web app demo  
RUN pip install Flask==0.10.1  
RUN pip install Flask-SQLAlchemy==2.0  
RUN pip install Jinja2==2.7.3  
RUN pip install MarkupSafe==0.23  
RUN pip install SQLAlchemy==0.9.9  
RUN pip install Werkzeug==0.10.4  
RUN pip install gunicorn==19.3.0  
RUN pip install itsdangerous==0.24  
RUN pip install flask-restful  
RUN pip install singularity  
  
# Install Singularity  
WORKDIR /tmp  
RUN git clone http://www.github.com/singularityware/singularity  
WORKDIR /tmp/singularity  
RUN git checkout -b lib-refactor  
RUN git pull origin lib-refactor  
RUN ./autogen.sh  
RUN ./configure --prefix=/usr/local  
RUN make  
RUN make install  
  
# Make directories for code and data  
RUN mkdir /code  
RUN mkdir /data  
  
# Add the code  
ADD . /code  
  
# Clean up  
RUN apt-get autoremove -y  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 8000  
WORKDIR /code  

