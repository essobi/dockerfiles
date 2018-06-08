FROM perl:5.26.1-threaded  
LABEL maintainer="Erik Hornyak <erik@recesscreative.com>"  
  
# App::cpanminus is now in the official perl Docker image  
# Use it to install Perl modules  
RUN cpanm Mojolicious  
RUN cpanm TryCatch  
RUN cpanm IO  
RUN cpanm EV  
RUN cpanm WebService::Rollbar::Notifier  
  
WORKDIR /root  
  
# COPY ["./perl.pl", "app/perl.pl"]  
# RUN ["chmod", "+x", "app/perl.pl"]  
# ENTRYPOINT ["app/perl.pl"]  
# #### MISCELLANEOUS TESTING #### #  
# CMD perl -E 'say "hello from perl at " . localtime()'  
# CMD icecream exec --port 8080 bin/perl.pl  
# CMD ["perl","perl.pl"]

