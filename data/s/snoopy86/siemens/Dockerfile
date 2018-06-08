FROM perl:latest  
COPY . /usr/src/myapp  
WORKDIR /usr/src/myapp  
  
RUN cpan LWP::UserAgent && \  
cpan LWP::Protocol::https && \  
cpan JSON && \  
cpan DBI  
  
CMD [ "perl", "./sendDataEmoncms.pl" ]

