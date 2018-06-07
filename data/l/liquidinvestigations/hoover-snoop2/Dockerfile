FROM python:3-stretch  
ENV PYTHONUNBUFFERED 1  
RUN set -e \  
&& echo 'deb http://deb.debian.org/debian stretch non-free' >>
/etc/apt/sources.list \  
&& echo 'deb http://deb.debian.org/debian stretch-updates non-free' >>
/etc/apt/sources.list \  
&& echo 'deb http://security.debian.org stretch/updates non-free' >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
p7zip-full p7zip-rar \  
cpanminus \  
poppler-utils \  
libgsf-1-dev \  
postgresql-client \  
&& cpanm --notest Email::Outlook::Message \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /opt/hoover/snoop  
WORKDIR /opt/hoover/snoop  
  
ADD requirements.txt ./  
RUN pip install -r requirements.txt  
  
RUN cd /opt \  
&& git clone https://github.com/hoover/magic-definitions.git \  
&& ( cd magic-definitions && ( ./build.sh ) && cp magic.mgc /opt/hoover/snoop/
)  
ENV PATH="/opt/magic-definitions/file/bin:${PATH}"  
RUN wget http://www.five-ten-sg.com/libpst/packages/libpst-0.6.71.tar.gz
--progress=dot:giga \  
&& tar zxvf libpst-0.6.71.tar.gz \  
&& rm -f libpst-0.6.71.tar.gz \  
&& mv libpst-0.6.71 /opt/libpst \  
&& cd /opt/libpst \  
&& ./configure --disable-python --prefix="`pwd`" \  
&& make \  
&& make install  
ENV PATH="/opt/libpst/bin:${PATH}"  
COPY . .  
  
RUN set -e \  
&& curl https://raw.githubusercontent.com/vishnubob/wait-for-it/8ed92e8c/wait-
for-it.sh -o /wait-for-it \  
&& echo '#!/bin/bash -e' > /runserver \  
&& echo 'waitress-serve --port 80 snoop.wsgi:application' >> /runserver \  
&& chmod +x /runserver /wait-for-it  
  
RUN ./manage.py collectstatic --noinput  
  
CMD /runserver  

