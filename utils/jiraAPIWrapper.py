from jira import JIRA
import requests                               
        
import os
        
from dotenv import load_dotenv         
        
load_dotenv()
        
project_key = "MOVIES"                   
             
class JiraAPI:                                  
    @classmethod
    def create_conn(cls):
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json"
        }                              
                    
        base_url = os.getenv("jira_base_url")
        token = os.getenv("jira_token")
        user_name = os.getenv("jira_user_name")
                    
        return cls(url=base_url, user=user_name, token=token)
                    
    def __init__(self, url, user, token):
        self.client = JIRA(url, basic_auth=(user, token))
        #print(self.client.search_issues("project=MOVIES"))
        #print(self.client.createmeta("MOVIES"))
        data = {
                "fields":
                {
                    "project":
                    {
                        "key": "MOVIES"
                    },
                    "parent":
                    {
                        "key": "DEMO-101"
                    },
                    "summary": "Sub-task of DEMO-101",
                    "description": "Don't forget to do this too because it is very important.",
                    "issuetype":
                    {
                        "id": "9"
                    }
                }
            }

    def get_projects(self):
        projects_list = []
        #print(self.client.projects())
        for prj in self.client.projects():
            projects_list.append(prj.key)

        return projects_list

    def issue(self, issueName):
        self.client.issue(issueName)
        issue = self.client.issue(issueName)
        return issue

    def get_issue(self, issueName):
        data = self.client.issue(issueName)
        return data

    def projects(self):
        projects = self.client.projects()
        return projects

    def add_comment(self, issueName, comment):
        # adds a comment to an existing ticket
        issue = self.client.add_comment(issueName, comment)
        return issue


    def create_issue(self, fields):
        #create_issue(fields: dict[str, Any] | None = None, prefetch: bool = True, **fieldargs)
        issue = self.client.create_issue(fields)
        return issue

    def add_user(self, username, email, directoryId, password, fullname, notify, active, ignore_existing):
        #Create a new Jira user.
        issue = self.client.add_user(username, email, directoryId, password, fullname, notify, active, ignore_existing)
        return issue

    def add_issues_to_epic(self, epic_id, issue_keys, ignore_epics):
        #Add the issues in issue_keys to the epic_id.
        issue = self.client.add_issues_to_epic(epic_id, issue_keys, ignore_epics)
        return issue

    def issue_update(self, summary, description):
     # Change the issue's summary and description.
        issue = self.client.issue_update(summary, description)
        return issue


    def create_project(self, key, name, id):
        #Create a project with the specified parameters.
        issue = self.client.create_project(key, name, id)
        return issue



moviejira = JiraAPI.create_conn()

moviejira.add_comment("MOVIES-4", "This is the latest update to end the week. The night crew is taking over from the afternoon shift guy and I am still working on the dev environment and hopefully this will be resolved soon.")


#moviejira.get_issue('MOVIES-3')

#moviejira.create_issue('fields')

# moviejira.create_issue(
#     fields = {
#         "project": {"key": "MOVIES"},
#         "issuetype": {"name": "Task"},
#         "summary": "Second Demo by Collins",
#         "description": "This is my Second Python Demo create issue created from Python code by collins orighose",
#     }
# )




