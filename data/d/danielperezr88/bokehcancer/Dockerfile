FROM danielperezr88/bokeh-python3:latest  
  
MAINTAINER danielperezr88 <danielperezr88@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
supervisor \  
git  
RUN mkdir -p /var/log/supervisor  
  
# Force pip2 installation and creation  
RUN curl -SL 'https://bootstrap.pypa.io/get-pip.py' | python2 \  
&& pip2 install --no-cache-dir --upgrade pip==$PYTHON_PIP_VERSION \  
&& cd / \  
&& curl -fSL
"https://gist.githubusercontent.com/danielperezr88/c3b7eb74c30d854f6db4b978a2f34582/raw/416a99ebddf210cf6f44173e79faeef98bfeb15d/pip_shebang_patch.txt"
\  
-o /pip_shebang_patch.txt \   
&& patch -p1 < pip_shebang_patch.txt  
  
RUN pip2 install supervisor && \  
pip2 install superlance==1.0.0  
  
# Download bokeh_cancer  
RUN curl -fSL
"https://github.com/danielperezr88/bokeh_cancer/archive/v1.5.tar.gz" -o
bokeh_cancer.tar.gz && \  
tar -xf bokeh_cancer.tar.gz -C . && \  
mkdir /app && \  
mv bokeh_cancer-1.5/* /app/ && \  
rm bokeh_cancer.tar.gz && \  
rm -rf bokeh_cancer-1.5 && \  
cp /app/supervisord.conf /etc/supervisor/conf.d/supervisord.conf && \  
rm /app/supervisord.conf  
  
# Copy apache config files  
RUN cp /app/apache-proxy-conf-files/000-default.conf /etc/apache2/sites-
available/000-default.conf && \  
cp /app/apache-proxy-conf-files/ports.conf /etc/apache2/ports.conf && \  
mkdir /var/log/apache2/bokeh  
  
# Download some custom config Gists to be applied to bokeh  
RUN curl -fSL
"https://gist.githubusercontent.com/danielperezr88/de9ecf70dd556a33f70e728cf58a54aa/raw/afb87786fb104401d42b1b57c3b26955c3fbac19/mod-
resources.py" > /usr/local/lib/python3.4/site-packages/bokeh/resources.py && \  
curl -fSL
"https://gist.githubusercontent.com/danielperezr88/90cd99575274f542cdb40ed0566fd0b0/raw/8e6b7d6a5ae53074eb5394cc295f8caa15e5f42c/BokehAppIndexTemplate.html"
> /usr/local/lib/python3.4/site-packages/bokeh/core/_templates/file.html  
  
RUN curl -sSO https://dl.google.com/cloudagents/install-logging-agent.sh -o
install-logging-agent.sh && \  
echo "07ca6e522885b9696013aaddde48bf2675429e57081c70080a9a1364a411b395
install-logging-agent.sh" | sha256sum -c \-  
  
EXPOSE 5006  
  
WORKDIR /app  
  
CMD ["/usr/bin/supervisord"]

