FROM sameersbn/redmine:3.4.4-2  
# patch irritating redirect after logging time to ticket  
RUN sed -i 's/redirect_back_or_default
project_time_entries_path(@time_entry.project)/redirect_to
issue_path(@time_entry.issue)/'
/home/redmine/redmine/app/controllers/timelog_controller.rb  
# patch versions form - show status field ALWAYS  
COPY _form.html.erb /home/redmine/redmine/app/views/versions/_form.html.erb  

