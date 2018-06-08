#  
# render-template Dockerfile  
#  
# https://github.com/jlesage/docker-render-template  
#  
# Pull base image.  
FROM alpine:3.6  
# Install dependencies.  
RUN \  
apk --no-cache add \  
python3 \  
py3-jinja2 \  
&& \  
pip3 install xmltodict requests  
  
# Add files.  
COPY render_template.py /usr/local/bin/  
  
# Set the entry point.  
ENTRYPOINT ["/usr/local/bin/render_template.py"]  
  
# Set default parameters to ENTRYPOINT.  
CMD ["-h"]  
  
# Metadata.  
LABEL \  
org.label-schema.name="render-template" \  
org.label-schema.description="Docker container to render Jinja2 templates
using JSON or XML file as data source" \  
org.label-schema.version="unknown" \  
org.label-schema.vcs-url="https://github.com/jlesage/docker-render-template" \  
org.label-schema.schema-version="1.0"  

