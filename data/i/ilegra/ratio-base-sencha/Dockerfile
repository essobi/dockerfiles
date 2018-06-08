FROM ilegra/java  
  
RUN mkdir /app  
WORKDIR /app  
  
COPY entrypoint.sh /bin/entrypoint.sh  
RUN chmod +x /bin/entrypoint.sh  
ENTRYPOINT [ "entrypoint.sh" ]  
CMD [ "compile" ]  
  
ADD https://s3.amazonaws.com/ratio-apt-repos/jars/SenchaCmd-6.1.2.15.sh.tar.gz
/  
COPY answers.txt /  
  
RUN locale-gen pt_BR.UTF-8  
ENV LC_ALL pt_BR.UTF-8  
RUN cd / \  
&& tar -zxvf SenchaCmd-6.1.2.15.sh.tar.gz \  
&& rm -vf SenchaCmd-6.1.2.15.sh.tar.gz \  
&& chmod +x SenchaCmd-6.1.2.15-linux-amd64.sh  
  
RUN /SenchaCmd-6.1.2.15-linux-amd64.sh --prefix /opt/Sencha/Cmd/6.1.2.15 <
/answers.txt \  
&& rm -vf /answers.txt \  
&& rm -vf /SenchaCmd-6.1.2.15-linux-amd64.sh  
  

