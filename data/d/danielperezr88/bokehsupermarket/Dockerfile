FROM danielperezr88/bokeh-python3:latest  
  
MAINTAINER danielperezr88 <danielperezr88@gmail.com>  
  
RUN apt-get update && apt-get install -y supervisor  
RUN mkdir -p /var/log/supervisor  
  
# Download bokeh_cancer  
RUN curl -fSL
"https://github.com/danielperezr88/bokeh_supermarket/archive/v0.3.tar.gz" -o
bokeh_supermarket.tar.gz && \  
tar -xf bokeh_supermarket.tar.gz -C . && \  
mkdir /app && \  
mv bokeh_supermarket-0.3/* /app/ && \  
rm bokeh_supermarket.tar.gz && \  
rm -rf bokeh_supermarket-0.3 && \  
cp /app/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
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
  
EXPOSE 5007  
  
CMD ["/usr/bin/supervisord"]  

