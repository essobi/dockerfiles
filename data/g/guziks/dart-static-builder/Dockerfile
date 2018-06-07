FROM google/dart:dev  
ONBUILD WORKDIR /app  
ONBUILD COPY pubspec.* ./  
ONBUILD RUN pub get  
ONBUILD COPY bin/ bin/  
ONBUILD COPY lib/ lib/  
ONBUILD RUN dart \  
\--snapshot=main.snap \  
bin/main.dart  

