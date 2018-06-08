FROM continuumio/anaconda3  
ENV PYTHONUNBUFFERED 1  
RUN apt-get update && apt-get install -y \  
libopenblas-dev \  
gfortran \  
pkg-config \  
build-essential \  
libxml2-dev \  
libxmlsec1-dev \  
libhdf5-dev \  
libgeos-dev \  
build-essential \  
libtool \  
autotools-dev \  
automake \  
autoconf \  
debootstrap \  
openssl \  
git \  
wget \  
vim  
  
  
RUN conda install -y cython numpy==1.13.1 \  
scikit-image==0.13.0 \  
scikit-learn==0.19.0 \  
scipy==0.19.1 \  
pandas==0.20.3 \  
h5py==2.7.0 \  
matplotlib==2.0.2 \  
numexpr==2.6.2 \  
networkx=1.11 \  
six==1.10.0  
  
RUN python -m pip install --upgrade pip  
RUN python -m pip install uwsgi \  
Pillow \  
pytz \  
celery==3.1.25 \  
Django==1.11.2 \  
django-celery==3.2.1 \  
django-chosen==0.1 \  
django-cleanup==1.0.1 \  
django-crispy-forms==1.6.1 \  
django-datatables-view==1.14.0 \  
django-dirtyfields==1.3 \  
django-filter==1.0.4 \  
django-form-utils==1.0.3 \  
django-gravatar2==1.4.2 \  
django-guardian==1.4.9 \  
django-hstore==1.3.5 \  
django-polymorphic==1.3 \  
django-rest-swagger==2.1.2 \  
django-sendfile==0.3.11 \  
django-taggit==0.22.1 \  
django-taggit-templatetags==0.2.5 \  
django-templatetag-sugar==1.0 \  
django-user-agents==0.3.2 \  
djangorestframework==3.6.4 \  
google==1.9.3 \  
google-api-python-client==1.6.4 \  
httplib2==0.10.3 \  
itsdangerous==0.24 \  
lxml==3.7.3 \  
numpy==1.13.1 \  
oauth2client==3.0.0 \  
oauthlib==2.0.4 \  
opbeat==3.5.2 \  
pkgconfig==1.2.2 \  
psycopg2==2.7.3.1 \  
pyasn1==0.3.6 \  
pyasn1-modules==0.1.4 \  
Pygments==2.2.0 \  
python-dateutil==2.6.0 \  
python3-openid==3.1.0 \  
python3-saml==1.3.0 \  
redis==2.10.6 \  
requests==2.14.2 \  
requests-oauthlib==0.8.0 \  
retrying==1.3.3 \  
Shapely==1.6.1 \  
simplejson==3.11.1 \  
singularity==1.2.0 \  
social-auth-app-django==1.2.0 \  
social-auth-core==1.4.0 \  
xmlsec==1.3.3  
  
RUN mkdir /code  
WORKDIR /code  
RUN /usr/bin/yes | python -m pip uninstall cython  
RUN apt-get remove -y gfortran  
  
RUN apt-get autoremove -y  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

