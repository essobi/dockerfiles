FROM petkr/torque-base  
  
COPY ./config /var/spool/torque/mom_priv/  
COPY entrypoint.sh /  
  
RUN chmod +x entrypoint.sh && \  
useradd testuser -u 9999  
  
EXPOSE 15002  
EXPOSE 15003  
ENTRYPOINT ["/entrypoint.sh"]

