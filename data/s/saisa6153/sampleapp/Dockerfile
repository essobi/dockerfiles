FROM saisa6153/sampleapp-base:latest  
MAINTAINER saisa6153  
USER root  
  
# nginx  
RUN mv /etc/nginx/nginx.conf ~  
ADD nginx.conf /etc/nginx/  
  
# supervisord  
ADD supervisord.conf /etc/  
  
# application  
WORKDIR /app  
ENV PATH /opt/ruby/bin:$PATH  
ADD SampleApp /app  
RUN bundle install --deployment  
ENV SECRET_KEY_BASE
75c7eb959bc7994feb7eb17bc76079cba5fc85121fd17a07ca57117450534a3ceda1729e8dca937a3d7f554f8e9f33ac16b98de3d2081938dddad7b4e49f4634  
  
EXPOSE 80  
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]

