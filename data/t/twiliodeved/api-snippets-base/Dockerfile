FROM twiliodeved/api-snippets-base:ruby  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
ENV RUN_ENV=test  
  
RUN git clone https://github.com/TwilioDevEd/twilio-api-faker.git /twilio-api-
faker && \  
cp /twilio-api-faker/keystore/twilio_fake.pem /usr/local/share/ca-
certificates/twilio_fake.crt && \  
update-ca-certificates  
  
RUN pip install virtualenvwrapper  
  
RUN composer global require overtrue/phplint && \  
ln -s /root/.composer/vendor/bin/phplint /usr/local/bin/phplint  
  
RUN mkdir /.virtualenvs  
  
ENV WORKON_HOME /.virtualenvs  
  
RUN echo 'source /usr/local/bin/virtualenvwrapper.sh' > ~/.bashrc  
  
RUN mkdir /src && git clone https://github.com/TwilioDevEd/api-snippets.git
/src  
  
COPY ./ /api-snippets-base  
  
WORKDIR /api-snippets-base  
  
RUN /bin/bash --login -c "make install_dependencies"  
  
RUN make build_api_faker  

