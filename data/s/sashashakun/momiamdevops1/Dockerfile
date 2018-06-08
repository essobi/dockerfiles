FROM nitive/rails  
  
RUN apt-get update && apt-get install -y nodejs  
  
ENV PROJECT_ROOT /app  
WORKDIR $PROJECT_ROOT  
  
ADD ./Gemfile* $PROJECT_ROOT/  
RUN bundle  
  
ADD . $PROJECT_ROOT/  

