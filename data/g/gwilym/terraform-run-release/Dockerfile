FROM hashicorp/terraform:0.10.8  
ENV TERRAFORM_VERSION="0.10.8"  
# note: can't use build args on dockerhub automated builds right now  
COPY include /opt/run-terraform-release  
RUN /opt/run-terraform-release/build.sh  
ENTRYPOINT ["/opt/run-terraform-release/run-terraform-release.sh"]  

