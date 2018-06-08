FROM smduarte/eclipse  
  
WORKDIR /tmp  
RUN git clone -b j8streams
https://smduarte@bitbucket.org/smduarte/altrande.git --single-branch && \  
unzip /tmp/altrande/AltranDockers/j8streams/j8streams.zip -d /home/me && \  
rm -rvf /tmp/altrande  
  
COPY ./eclipse_init.sh /  
RUN chmod a+x /eclipse_init.sh  
RUN chmod -R a+w /home/me/j8streams  
CMD [ "/eclipse_init.sh" ]

