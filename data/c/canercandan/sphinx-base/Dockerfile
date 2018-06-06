FROM canercandan/python3-base  
MAINTAINER Caner Candan <caner@candan.fr>  
  
WORKDIR /tmp  
  
# install all dependencies  
RUN apt-get -qq update  
RUN apt-get -qqy install python3-numpy python3-matplotlib ipython3 nginx-
extras git curl openjdk-7-jre-headless wget unzip  
  
# install ditaa + plantuml  
RUN { \  
cd /opt; \  
wget http://sourceforge.net/projects/plantuml/files/plantuml.8007.jar/download
-O plantuml.jar; \  
wget http://sourceforge.net/projects/ditaa/files/latest/download -O ditaa.zip;
\  
unzip ditaa.zip && mv ditaa*.jar ditaa.jar; \  
}  
RUN { \  
echo '#! /bin/sh'; \  
echo 'exec java -jar /opt/plantuml.jar "$@"'; \  
} > /usr/bin/plantuml && chmod +x /usr/bin/plantuml  
RUN { \  
echo '#! /bin/sh'; \  
echo 'exec java -jar /opt/ditaa.jar "$@"'; \  
} > /usr/bin/ditaa && chmod +x /usr/bin/ditaa  
  
# install sphinx + dependencies  
RUN pip install -q sphinx sphinx_rtd_theme numpydoc sphinxcontrib-plantuml
sphinxcontrib-actdiag sphinxcontrib-blockdiag sphinxcontrib-nwdiag
sphinxcontrib-seqdiag  
  
# install sphinx-ditaa  
RUN { \  
git clone https://github.com/w-vi/sphinx-ditaa; \  
cd sphinx-ditaa; \  
python setup.py install; \  
}  
  
WORKDIR /doc  
  
VOLUME /doc  
  
# setup nginx  
RUN { \  
echo; \  
echo '# stay in the foreground so Docker has a process to track'; \  
echo 'daemon off;'; \  
} >> /etc/nginx/nginx.conf  
  
RUN { \  
echo 'server {'; \  
echo 'server_name localhost;'; \  
echo 'listen 80 default_server;'; \  
echo 'charset utf-8;'; \  
echo 'root /doc;'; \  
echo '}'; \  
} > /etc/nginx/sites-enabled/default  
  
# run  
EXPOSE 80  
CMD ["nginx"]  

