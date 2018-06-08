FROM debian:stretch-slim  
  
MAINTAINER qqbuby <qqbuby@gmail.com>  
  
ENV RTD_REPO_DIR=/var/readthedocs \  
RTD_COMMIT=2a54e3adf487412f58a0a4473c0a52250b15ff18  
  
# ADD ./sources.list /etc/apt/sources.list  
# ADD ./pip.conf ~/.pip/pip.conf  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
curl \  
git \  
libxml2-dev \  
libxslt1-dev \  
libz-dev \  
python-dev \  
python-pip \  
python-setuptools \  
texlive-latex-recommended \  
texlive-fonts-recommended \  
texlive-formats-extra \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -ksSL
https://github.com/rtfd/readthedocs.org/archive/$RTD_COMMIT.tar.gz | tar xz -C
/tmp/ \  
&& mkdir -p ${RTD_REPO_DIR} \  
&& mv /tmp/readthedocs.org-${RTD_COMMIT}*/*
/tmp/readthedocs.org-${RTD_COMMIT}*/.??* ${RTD_REPO_DIR} \  
&& rm -rf /tmp/readthedocs.org-${RTD_COMMIT}*  
  
WORKDIR ${RTD_REPO_DIR}  
  
RUN pip install wheel \  
&& pip install -r requirements.txt \  
&& pip install --upgrade pip \  
&& rm -rf ~/.cache /tmp/pip_build_root  
  
RUN python ./manage.py migrate  
  
ADD ./init.py .  
RUN python init.py  
  
RUN python ./manage.py collectstatic --noinput  
  
EXPOSE 8000  
CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000"]  

