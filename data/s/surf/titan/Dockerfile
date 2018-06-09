# Titan  
#  
# VERSION 0.0.1  
# BUILD-USING: docker build -t titan .  
# PUSH-USING: docker tag titan surf/titan && docker push surf/titan  
FROM surf/base-jvm  
MAINTAINER Dan Kinsley <dan@surfbeta.com>  
  
# download and install titan server  
RUN curl --silent
http://s3.thinkaurelius.com/downloads/titan/titan-0.5.0-hadoop2.zip --output
titan-server.zip  
RUN unzip -qq /titan-server.zip  
RUN ln -s /titan-0.5.0-hadoop2 /titan-server  
RUN chown daemon:daemon /titan-server  
  
ADD run.py /run.py  
RUN chmod u+x /run.py  
# Port for RexPro  
EXPOSE 8182 8183 8184 8185  
# Launch titan when launching the container  
CMD ["/run.py"]  

