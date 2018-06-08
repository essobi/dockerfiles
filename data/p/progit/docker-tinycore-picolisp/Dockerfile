FROM tatsushid/tinycore:8.0-x86_64  
  
RUN sudo adduser -D pil  
COPY pil.tgz /home/pil/pil.tgz  
  
RUN sudo tar -xvzf /home/pil/pil.tgz -C /home/pil \  
&& sudo ln -s /home/pil/picoLisp /usr/lib/picolisp \  
&& sudo ln -s /usr/lib/picolisp/bin/picolisp /usr/bin \  
&& sudo ln -s /usr/lib/picolisp/bin/pil /usr/bin  
  
EXPOSE 8080  
  
USER pil  
CMD [ "pil", "+" ]  

