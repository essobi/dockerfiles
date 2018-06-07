FROM ruby:2.2.0  
ADD init_homesick.sh /tmp/init_homesick.sh  
RUN chmod 755 /tmp/init_homesick.sh  
RUN gem install homesick  
  
ENTRYPOINT ["/tmp/init_homesick.sh"]  
  
CMD ["/bin/bash"]  

