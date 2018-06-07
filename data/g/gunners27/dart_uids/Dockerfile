FROM google/dart  
  
WORKDIR /dart_uids_service  
  
ADD pubspec.* /dart_uids_service/  
RUN pub get  
ADD . /dart_uids_service  
RUN pub get --offline  
  
CMD ["dart", "bin/main.dart"]

