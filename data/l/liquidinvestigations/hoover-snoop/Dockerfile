FROM python:3  
ENV PYTHONUNBUFFERED 1  
RUN set -e \  
&& echo 'deb http://deb.debian.org/debian jessie non-free' >>
/etc/apt/sources.list \  
&& echo 'deb http://deb.debian.org/debian jessie-updates non-free' >>
/etc/apt/sources.list \  
&& echo 'deb http://security.debian.org jessie/updates non-free' >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
p7zip-full p7zip-rar \  
pst-utils \  
cpanminus \  
poppler-utils \  
&& cpanm --notest Email::Outlook::Message \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /opt/hoover/snoop  
WORKDIR /opt/hoover/snoop  
  
ADD requirements.txt ./  
RUN pip install -r requirements.txt  
  
COPY . .  
  
RUN set -e \  
&& curl https://raw.githubusercontent.com/vishnubob/wait-for-it/8ed92e8c/wait-
for-it.sh -o /wait-for-it \  
&& echo '#!/bin/bash -e' > /runserver \  
&& echo 'waitress-serve --port 80 snoop.site.wsgi:application' >> /runserver \  
&& chmod +x /runserver /wait-for-it  
  
CMD /runserver  

