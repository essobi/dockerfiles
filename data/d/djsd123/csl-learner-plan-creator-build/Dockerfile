FROM djsd123/csl-learner-plan-creator-build:v2  
MAINTAINER Mikael Allison <mikael.allison@digital.cabinet-office.gov.uk>  
USER dev  
WORKDIR /home/dev/learner_plan_creator/  
RUN git pull https://github.com/crossgovernmentservices/csl-learner-plan-
creator.git  
RUN pip install -r /home/dev/learner_plan_creator/requirements/dev.txt  
ONBUILD WORKDIR /home/dev/learner_plan_creator/  
ONBUILD RUN git pull https://github.com/crossgovernmentservices/csl-learner-
plan-creator.git && pip install -r
/home/dev/learner_plan_creator/requirements/dev.txt  
EXPOSE 8000  
CMD ["./run_prod.sh", "8000"]

