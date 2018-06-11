FROM alpine  
  
RUN apk add --update --no-cache ansible  
  
ENTRYPOINT ["ansible-playbook"]  
CMD ["site.yml"]  

