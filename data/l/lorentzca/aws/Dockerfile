FROM alpine:3.6  
ARG pip_installer="https://bootstrap.pypa.io/get-pip.py"  
ARG awscli_version="1.11.130"  
# Install dependent packages  
RUN apk --update add \  
python \  
curl \  
groff  
  
# Install awscli  
RUN curl ${pip_installer} | python && \  
pip install awscli==${awscli_version}  
  
# Execute aws command  
ENV PAGER="less"  
ENTRYPOINT ["/usr/bin/aws"]  
CMD ["help"]  

