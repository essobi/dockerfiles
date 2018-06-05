# MySQL-python does not support python 3 yet.  
FROM python:2-onbuild  
# Add Tini  
ENV TINI_VERSION v0.9.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "--"]  
  
# Exposes port 10053 by default  
EXPOSE 10053 10053/udp  
  
# Run python  
CMD ["python", "./dns.py"]  

