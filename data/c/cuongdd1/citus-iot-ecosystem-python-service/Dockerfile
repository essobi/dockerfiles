# Start with a python base image with some Python libs preinstalled  
FROM python:3.6.2-alpine3.6  
# Add the scotch py-service  
COPY service.py /opt/cloud-apps/  
COPY utilities.py /opt/cloud-apps/  
COPY static /opt/cloud-apps/static/  
COPY entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
  
# Install latest stable dependancies  
RUN apk add --update && pip --no-cache-dir install requests simplejson flask
boto3 uuid &&\  
rm -rf /var/lib/apt/lists/* &&\  
rm -rf /var/cache/apk/*  
  
VOLUME /opt/cloud-apps  
VOLUME /opt/cloud-apps/static/apis  
  
# Rest API  
EXPOSE 5000  
# Tell the kernel gateway to load the scotch notebook by default  
CMD ["/entrypoint.sh", "--allow-root"]  

