# CfnCluster v1.3  
#  
# docker run \--rm pottava/cfncluster:1.3 version  
# docker run \--rm \--entrypoint cat pottava/cfncluster:1.3
/root/.cfncluster/config  
# docker run \--rm -it -v `pwd`:/root/.cfncluster pottava/cfncluster:1.3
configure  
# docker run \--rm -it -v `pwd`:/root/.cfncluster pottava/cfncluster:1.3
create <cluster-name>  
# docker run \--rm -it -v `pwd`:/root/.cfncluster pottava/cfncluster:1.3 list  
  
FROM alpine:3.6  
  
RUN apk --no-cache add python  
  
RUN apk --no-cache add --virtual build-dependencies py2-pip \  
&& apk --no-cache add py-setuptools groff jq \  
  
&& pip install 'cfncluster == 1.3.2' \  
&& pip install 'awscli == 1.11.167' \  
&& mkdir /root/.cfncluster \  
&& cp /usr/lib/python2.7/site-packages/cfncluster/examples/config
/root/.cfncluster/config \  
  
&& apk del --purge -r build-dependencies \  
&& find / -type d -name tests -depth -exec rm -rf {} \; \  
&& find / -type d -name test -depth -exec rm -rf {} \; \  
&& find / -type d -name examples -depth -exec rm -rf {} \; \  
&& rm -rf /root/.cache  
  
ENTRYPOINT ["cfncluster"]  
CMD ["-h"]  

