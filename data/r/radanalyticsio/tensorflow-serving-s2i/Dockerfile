FROM openshift/base-centos7  
  
MAINTAINER Subin Modeel smodeel@redhat.com  
  
ENV BUILDER_VERSION 1.0  
LABEL io.k8s.description="Tensorflow serving builder" \  
io.k8s.display-name="tensorflow serving builder" \  
io.openshift.expose-services="6006:http" \  
io.openshift.tags="tensorflow"  
  
RUN yum install -y tree which \  
&& yum clean all -y  
  
COPY ./s2i/bin/ /usr/libexec/s2i  
  
#Drop the root user and make the content of /opt/app-root owned by user 1001  
RUN chown -R 1001:1001 /opt/app-root  
  
# This default user is created in the openshift/base-centos7 image  
USER 1001  
COPY ./tensorflow_model_server /opt/app-root/tensorflow_model_server  
  
# EXPOSE 6006  
# TODO: Set the default CMD for the image  
CMD ["/usr/libexec/s2i/usage"]  

