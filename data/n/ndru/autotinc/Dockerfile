FROM ndru/tinc  
  
ADD autotinc.sh /autotinc.sh  
RUN chmod +x /autotinc.sh  
  
EXPOSE 655/tcp 655/udp  
  
ENTRYPOINT ["/autotinc.sh"]  
CMD ["start"]  

