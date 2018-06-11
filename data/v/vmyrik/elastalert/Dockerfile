FROM python:2  
LABEL maintainer="Vitalii Muravitskiy, https://github.com/muravitskiy"  
  
ENV ELASTALERT_VERSION=0.1.27  
ENV ELASTALERT_CONFIG="config.yaml"  
RUN pip install elastalert==${ELASTALERT_VERSION}  
  
COPY ./entrypoint.sh ./  
RUN chmod +x ./entrypoint.sh  
  
ENTRYPOINT ["./entrypoint.sh"]  
  
CMD ["elastalert", "--verbose"]  

