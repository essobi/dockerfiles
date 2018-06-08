FROM alpine:latest  
  
COPY make_imapfilter_and_clean.sh /  
  
# Make and remove make resources in one step to keep small image layers  
RUN source /make_imapfilter_and_clean.sh  
  
CMD ["imapfilter"]  

