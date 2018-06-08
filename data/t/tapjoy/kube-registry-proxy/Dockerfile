FROM gcr.io/google_containers/kube-registry-proxy:0.4  
MAINTAINER Brent Stephens  
  
EXPOSE 5000  
RUN sed -i s/"PORT=80"/"PORT=5000"/g /bin/boot  

