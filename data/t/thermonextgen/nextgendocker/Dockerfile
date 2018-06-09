FROM microsoft/dotnet:2.0.5-runtime AS base  
  
RUN apt-get update && apt-get install -y unzip  
#RUN apt-get update && apt-get install -y vim  
RUN apt-get update && apt-get install -y libexpat1  
  
RUN apt-get update && apt-get install -y python3  
RUN curl -O https://bootstrap.pypa.io/get-pip.py  
RUN python3 get-pip.py  
ENV PATH=$PATH:~/.local/bin  
  
RUN pip3 install awscli --upgrade --user  
  
WORKDIR /app  
copy ./run_aws_app.sh ./  
copy ./run_aws_app_singlefile.sh ./  
copy ./run_aws_app_singlefile_app_params_only.sh ./  
  
RUN chmod 755 run_aws_app.sh  
RUN chmod 755 run_aws_app_singlefile.sh  
RUN chmod 755 run_aws_app_singlefile_app_params_only.sh  
  
# usage of this docker image will be docker run <imageName>
<aws_s3_input_file> <aws_s3_output_file>  
# applications/algorithms will go into the container /app folder  
# input files will be automatically copied into the container /appinputs
folder  
# add the commented entry point line below to any inherited docker image  
# edit the last 2 parameters "image path to your exe", "image path to your
application output"  
# example to exe /app/tandem.exe  
# example to output /appinputs/output.xml - this is the output that
application produces locally, not the file copied to AWS.  
#ENTRYPOINT ["/app/run_aws_app.sh", "image-path-to-your-exe", "image-path-to-
the-local-app-output-file"]  

