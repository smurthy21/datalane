# datalane

datalane is an easy to use, command line, python package which helps in designing and controlling data pipelines 
in data engineering world. Users can see a significant cutdown in workflow development time and can spend quality time on 
developing business logic necessary for data pipelines.

It accepts a workflow defintion in the form of yml and supports various features as described in the below sections.

#### Installation

Clone the repo.
Run ```python setup.py install``` in your personal python3 virtual env.

#### Features

Here are some of the features that we are planning to support in initial versions:
1. Run various tasks of a workflow in predetermined sequence.
2. Workflow order is provided as a list of lists and can have serial and parallel tasks. Here is a sample workflow order
   ```[serialtask1, serialtask2, [paralleltask3, paralleltask4], serialtask5]``` If any of the task fails, the workflow
   would enter failed status and terminates. If any one of the parallel tasks fail, the workflow waits for the other 
   parallel tasks within the stage to complete and then exit. Workflow state is captured so that workflow starts from
   point of failure upon restart (of course in parallel tasks stage, only the failed parallel tasks rerun).
3. Provide an option to kick off the entire workflow in case of any failure.
4. User will be allowed to pass runtime context variables either in the dict format at the cli or in a yml format.
5. Uses SQLAlchemy and can run sqls against MySQL, postgres.      


Following are the tasks that would be supported until the application is stable:
1. BatchCommand
2. SQLCommand
3. SQLFile
4. SQLValidator
5. SendEmail

We will update new features as and when they are available.

##### A sample workflow yml
```
context:  
   repo: /var/loc/to/custom/repo

wf_name: sample_datalane_wkf

wf_order: [  
           'clear_loc_dir' ,   
           'make_api_call',  
           ['load_table1', 'load_table2'] # Parallel Tasks  
           'load_final_table'  
           ]

clear_loc_dir:  
  type: BatchCommand  
  cmd: rm -rf /var/dir/tmp/custom_dir  

make_api_call:  
  type: BatchCommand  
  cmd: python /var/loc/to/repo/dir/api_extract.py start_date=${st_input_date} end_date=${end_input_date}

load_locations:  
  conn: de_db_conn  
  sql:  
      - insert into ${target_db}.locations as select * from ${stage}.stg_locations;
    
load_products:  
  conn: de_db_conn  
  sql:  
      - insert into ${target_db}.products as select * from ${stage}.products;  

load_products:  
  conn: de_db_conn  
  sqlfile:  
          ${repo}/incremental/sales/final.sql
```


