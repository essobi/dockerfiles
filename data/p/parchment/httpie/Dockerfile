FROM alpine:3.6  
RUN set -x \  
&& apk add --no-cache \  
bash \  
python3 \  
&& pip3 install --upgrade \  
pip \  
setuptools \  
httpie \  
&& rm -r /root/.cache  
  
ENTRYPOINT ["bash"]  
CMD ["-c", "http --help"]  
  
LABEL org.label-schema.schema-version="1.0" \  
org.label-schema.name="HTTPie" \  
org.label-schema.description="HTTPie on Alpine" \  
org.label-schema.url="https://httpie.org/"  

